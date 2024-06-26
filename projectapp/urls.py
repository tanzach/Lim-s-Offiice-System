"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'), 
    path('homepage', views.homepage, name='homepage'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout_view, name='logout'),

    path('manage_account', views.manage_account, name='manage_account'),
    path('homepage_office', views.homepage_office, name='homepage_office'),
    path('edit_account/<int:pk>/', views.edit_account, name='edit_account'),
    path('view_inventory', views.view_inventory, name='view_inventory'),
    path('view_orders', views.view_orders, name='view_orders'),
    path('view_customers', views.view_customers, name='view_customers'),
    path('new_customer', views.new_customer, name='new_customer'),

    path('edit_customer/<int:pk>/', views.edit_customer, name='edit_customer'),
    path('delete_customer/<int:pk>/', views.delete_customer, name='delete_customer'),
    path('delete_account/<int:pk>/', views.delete_account, name='delete_account'),

    path('create_customer_order', views.create_customer_order, name='create_customer_order'),
    path('edit_order/<int:pk>/', views.edit_order, name='edit_order'),
    path('customer_order/<int:pk>/', views.customer_order, name='customer_order'),
    path('add_products', views.add_products, name='add_products'), 
    path('edit_inventory/<int:pk>/', views.edit_inventory, name='edit_inventory'),
    path('delete_inventory/<int:pk>/', views.delete_inventory, name='delete_inventory'),
    path('decline_payment/<int:pk>/', views.decline_payment, name='decline_payment'),
    path('approve_payment/<int:pk>/', views.approve_payment, name='approve_payment'),
    path('ready_for_delivery/<int:pk>/', views.ready_for_delivery, name='ready_for_delivery'),
    path('delete_order/<int:pk>/', views.delete_order, name='delete_order'),
    path('get_latest_discount/<int:customer_id>/<int:product_id>/', views.get_discount, name='get_latest_discount'),

    path('homepage_warehouse', views.homepage_warehouse, name='homepage_warehouse'),
    path('edit_inventory_warehouse/<int:pk>/', views.edit_inventory_warehouse, name='edit_inventory_warehouse'),
    path('view_orders_warehouse', views.view_orders_warehouse, name='view_orders_warehouse'),
    path('customer_order_warehouse', views.customer_order_warehouse, name='customer_order_warehouse'),
    path('view_inventory_warehouse', views.view_inventory_warehouse, name='view_inventory_warehouse'),
    path('edit_order_warehouse', views.edit_order_warehouse, name='edit_order_warehouse'),
    path('customer_order_owner/<int:pk>/', views.customer_order_owner, name='customer_order_owner'),
    path('view_inventory_owner', views.view_inventory_owner, name='view_inventory_owner'),
    path('view_customers_owner', views.view_customers_owner, name='view_customers_owner'),
    path('view_orders_owner', views.view_orders_owner, name='view_orders_owner'),
]
