function fill_product(productElement) {
    var selectElement = $(productElement);
    var selectedOption = selectElement.find("option:selected");
    var unit = selectedOption.data("unit");
    var unitprice = selectedOption.data("price");
    var quantity = 0;
    var aqcode = selectedOption.data("aqcode");
    var amount = 0;
    selectElement.closest(".form-field").find("#unit").val(unit);
    selectElement.closest(".form-field").find("#unitprice").val(unitprice);
    selectElement.closest(".form-field").find("#quantity").val(quantity);
    selectElement.closest(".form-field").find("#acquisitioncode").val(aqcode);
    selectElement.closest(".form-field").find("#amount").val(amount.toFixed(2));
}

function fill_product_added_row(productElement) {
    var selectElement = $(productElement);
    var selectedOption = selectElement.find("option:selected");
    var unit = selectedOption.data("unit");
    var unitprice = selectedOption.data("price");
    var quantity = 0 
    var aqcode = selectedOption.data("aqcode");
    var amount = 0;
    selectElement.closest("#rowfield").find("#unit").val(unit);
    selectElement.closest("#rowfield").find("#unitprice").val(unitprice);
    selectElement.closest("#rowfield").find("#quantity").val(quantity);
    selectElement.closest("#rowfield").find("#acquisitioncode").val(aqcode);
    selectElement.closest("#rowfield").find("#amount").val(amount.toFixed(2));
}

// function fill_product() {
//     var selectElement = document.getElementById("productname");
//     var selectedOption = selectElement.options[selectElement.selectedIndex];
//     var unit = selectedOption.getAttribute("data-unit");
//     var unitprice = selectedOption.getAttribute("data-price");
//     var aqcode = selectedOption.getAttribute("data-aqcode");
//     document.getElementById("unit").value = unit;
//     document.getElementById("acquisitioncode").value = aqcode;
//     document.getElementById("unitprice").value = unitprice;
// }

function fill_price(productElement) {
    var selectElement = $(productElement);
    var price = parseFloat(document.getElementById("unitprice").value);
    var quantity = parseFloat(document.getElementById("quantity").value);
    var discount = parseFloat(document.getElementById("discount").value);
    var discountfactor = 1 - discount;
    var amount = parseFloat(price * quantity * discountfactor); 
    selectElement.closest(".form-field").find("#amount").val(amount.toFixed(2));
}

function fill_price_added_row(productElement) {
    var selectElement = $(productElement);
    var price = parseFloat(selectElement.closest("#rowfield").find("#unitprice").val());
    var quantity = parseFloat(selectElement.closest("#rowfield").find("#quantity").val());
    var discount = parseFloat(selectElement.closest("#rowfield").find("#discount").val());
    var discountfactor = 1 - discount;
    var amount = parseFloat(price * quantity * discountfactor); 
    selectElement.closest("#rowfield").find("#amount").val(amount.toFixed(2));
}

// function fill_total_price() {
//     var totalprice = parseFloat(document.getElementById("amount").val());
//     document.getElementById("totalprice").value = totalprice.toFixed(2);
// }

$(document).ready(function() {
    function updateTotalPrice() {
        var totalPrice = 0; // Initialize total price
        // Iterate over all the amount fields and sum up their values
        $('.form-field').each(function() {
            var amount = parseFloat($(this).find("#amount").val()); // Get the value of each amount field
            if (!isNaN(amount)) { // Check if the value is a valid number
                totalPrice += amount; // Add the amount value to the total price
            }
        });

        // Update the total price field with the computed total
        $('#totalprice').val(totalPrice.toFixed(2));
    }

    updateTotalPrice();

    // Event listener to update total price when quantity fields change
    $(document).on('input', '.form-field input[type="number"]', function() {
        var inputField = $(this);
        // Wait for 100 milliseconds before calling updateTotalPrice
        setTimeout(function() {
            updateTotalPrice(); // Call the updateTotalPrice function after a slight delay
        }, 100);
    });

    // Event listener for customer selection change
    $('#customer').change(function() {
        customerId = $(this).val(); // Update customerId globally
    });

    // Event listener for product selection change
    $('#productname').change(function() {
        var row = $(this).closest('.form-field'); // Find the parent row
        var productId = $(this).val(); // Get the selected product ID
        fillLatestDiscount(customerId, productId, row); // Fill latest discount
    });

    $("#addButton").click(function(e){
        e.preventDefault();
        // Ensure customerId is set before making AJAX request
        var productId = $('#productname').val(); // Get the selected product ID
        var container = $("#rowfield").last();
        $("#rowfield").last().after(`
            <div class="form-field d-flex justify-content-center" id="rowfield">
                <div class="container">
                    <div class="row mt-1"> 
                        <div class="col-2" style="padding-right: 10px;"> 
                            <select class="form-select" id="productname" name="productname" placeholder="Product Name" onchange="fill_product_added_row(this)" required>
                                <option value="" selected disabled> Choose here... </option>
                            {% for p in products %}
                                <option value="{{p.Product_ID}}" data-unit="{{p.Unit}}" data-price="{{p.Unit_Price}}" data-aqcode="{{p.Acquisition_Code}}"> {{p.Product_Name}} </option>
                            {% endfor %}

                            </select>
                        </div>
                            
                        <div class="col" style="padding-left: 0; padding-right: 10px;">
                            <input type="text" class="form-control" id="unit" name="unit" placeholder="Unit" readonly required>
                        </div>

                        <div class="col" style="padding-left: 0; padding-right: 10px;">
                            <input type="text" class="form-control" inputmode="numeric" id="unitprice" name="unitprice" placeholder="Unit Price" onchange="fill_price_added_row(this)" required>
                        </div>
                        <div class="col" style="padding-left: 0; padding-right: 10px;">
                            <input type="number" class="form-control" inputmode="numeric" id="quantity" name="quantity" placeholder="Quantity" onchange="fill_price_added_row(this)" min="1" step="1" required>
                        </div>
                        <div class="col-2" style="padding-left: 0; padding-right: 10px;">
                            <input type="text" class="form-control" id="acquisitioncode" name="acquisitioncode" placeholder="Acquisition Code" readonly required>
                        </div>
                        <div class="col" style="padding-left: 0; padding-right: 10px;"> 
                            <input type="number" class="form-control" inputmode="numeric" id="discount" name="discount" placeholder="Discount" onchange="fill_price_added_row(this)" min="0" step="0.01" value="0">
                        </div>
                        <div class="col" style="padding-left: 0; padding-right: 10px;"> 
                            <input type="text" class="form-control" inputmode="numeric" id="amount" name="amount" placeholder="Amount" required>
                        </div>
                        <div class="col" style="padding-left: 0; padding-right: 0;"> 
                            <button type="button" class="btn btn-danger deleteButton"> Delete </button>
                        </div>
                    </div>
                </div>
            </div>`
        );

        // Get the container of the newly added row field
        var container = $("#rowfield").last();

        // Get the product ID from the newly added row field
        var productId = container.find("#productname").val();
        
        // Call fillLatestDiscount with the appropriate parameters
        fillLatestDiscount(customerId, productId, container);
    });

    $(document).on('click', '.deleteButton', function(e) {
        e.preventDefault();
        $(this).closest('#rowfield').remove();
        updateTotalPrice();
    });

    $('#customer').change(function() {
        customerId = $(this).val(); // Update customerId globally
    });

    // Event listener for product selection change
    $('#productname').change(function() {
        var row = $(this).closest('.form-field'); // Find the parent row
        var productId = $(this).val(); // Get the selected product ID
        fillLatestDiscount(customerId, productId, row); // Fill latest discount
    });

});

// function deleteField(productElement){
//     var selectedElement = $(productElement);
//     selectedElement.closest(".rowfield").remove();
// }

// Event listener for form submission
$('#myForm').submit(function(e) {
    // This prevents the form from submitting normally
    e.preventDefault();

    // Check if any form fields are empty
    var isEmpty = false;
    $('.form-field').each(function() {
        var quantity = $(this).find("#quantity").val();
        if (!quantity || parseInt(quantity) <= 0) {
            isEmpty = true;
            return false; // Exit the loop early if an empty field is found
        }
    });

    // If any field is empty, prevent form submission
    if (isEmpty) {
        alert("Please fill in all quantity fields with a value greater than 0.");
        return;
    }

    // Collect and store rowfield data
    var formData = [];
    $('.form-field').each(function() {
        var data = {
            product_id: $(this).find("#productname").val(),
            unit: $(this).find("#unit").val(),
            unit_price: $(this).find("#unitprice").val(),
            quantity: $(this).find("#quantity").val(),
            acquisition_code: $(this).find("#acquisitioncode").val(),
            discount: $(this).find("#discount").val(),
            amount: $(this).find("#amount").val()
        };
        formData.push(data);
        console.log(formData);
    });

    // Append formData as a hidden field in the form
    $('<input>').attr({
        type: 'hidden',
        name: 'formData',
        value: JSON.stringify(formData) // Convert to JSON string
    }).appendTo('#myForm');

    // Submit the form
    this.submit();

});

$(document).ready(function() {
    console.log('Parsely initialized');
    $('#myForm').parsley();
});

function fillLatestDiscount(customerId, productId, container) {
// Find the row corresponding to the selected product ID
var row = $('#productname option:selected[value="' + productId + '"]').closest('.form-field');
// Find the discount field within the same row
var discountInput = row.find("#discount");

// AJAX request to fetch the latest discount
$.ajax({
    url: `/get_latest_discount/${customerId}/${productId}`,
    type: 'GET',
    success: function(response) {
        // Handle the response from the server
        console.log(response);
        // Update the discount field with the received discount value
        var latestDiscount = response.discount;
        container.find("#discount").val(latestDiscount);
        // discountInput.val(latestDiscount); // Assuming the ID of the discount field is 'discount'
        console.log(latestDiscount);
    },
    error: function(xhr, errmsg, err) {
        // Handle any errors
        console.log(xhr.status + ": " + xhr.responseText); // Log the error message
    }
});
}

// Event listener for customer and product selection change
$('#customer, #productname').change(function() {
var row = $(this).closest('.form-field');
var customerId = $('#customer').val();
var productId = $(this).val();
fillLatestDiscount(customerId, productId, row);
});

$(document).ready(function() {
// Event listener for customer selection change
$('#customer').change(function() {
    customerId = $(this).val(); // Update customerId globally
    var productId = $('#productname').val();
    fillLatestDiscount(customerId, productId);
});
});