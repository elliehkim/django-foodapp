from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse

class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(null=True)
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to='item_images',blank=True,null=True)

    def __str__(self):
        return self.name
    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete= models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.item.price

STATUS_CHOICE = (
    ('Preparing', 'Preparing'),
    ('On the way', 'On the way'),
    ('Delievered','Delievered')
)

class OrderDetails(models.Model):
    order_number = models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    zipcode = models.IntegerField()

class Order(models.Model):
    order_number = models.IntegerField(null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)
    status = models.CharField(max_length=50, choices=STATUS_CHOICE, default='Preparing')

    @property
    def total_cost(self):
        return self.quantity * self.item.price
