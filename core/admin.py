from django.contrib import admin
from .models import Item, Cart, Order, OrderDetails

admin.site.register(Item)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderDetails)

# Register your models here.

