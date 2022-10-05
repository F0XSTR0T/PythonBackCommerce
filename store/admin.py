from django.contrib import admin
from store.models import Order, Product, Cart


admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Cart)
