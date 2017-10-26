from django.contrib import admin

# Register your models here.
from .models import ChartOfAccounts, ProductList, Crew, Products, VoucherInfo, JV, CDV, CRV, Branch, Sales


admin.site.register(ChartOfAccounts)
admin.site.register(ProductList)
admin.site.register(Crew)
admin.site.register(Products)
admin.site.register(VoucherInfo)
admin.site.register(JV)
admin.site.register(CDV)
admin.site.register(CRV)
admin.site.register(Branch)
admin.site.register(Sales)