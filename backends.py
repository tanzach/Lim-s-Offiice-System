# from django.contrib.auth.backends import BaseBackend
# from .models import Account

# class AccountBackend(BaseBackend):
#     def authenticate(self, request, employee_id=None, password=None):
#         try:
#             account = Account.objects.get(Employee_ID=employee_id)
#             if account.password == password:
#                 return account
#         except Account.DoesNotExist:
#             return None

#     def get_user(self, user_id):
#         try:
#             return Account.objects.get(pk=user_id)
#         except Account.DoesNotExist:
#             return None