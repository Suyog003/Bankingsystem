from django.contrib import admin
from .models import customer,transactions
# Register your models here.
admin.site.register(customer)
admin.site.register(transactions)