from django.contrib import admin
from .models import Product, SavingsProduct, Category


admin.site.register(Product)
admin.site.register(SavingsProduct)
admin.site.register(Category)
