from django.db import models


# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    contact_no = models.CharField(max_length=15)
    pincode = models.CharField(max_length=25)

    def __str__(self):
        return self.first_name


class Product(models.Model):
    name = models.CharField(max_length=150, null=True, default="xyz")
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer_id = models.ForeignKey(Customer, verbose_name="Customer",on_delete=models.SET_NULL, null=True, blank=True)
    product_id = models.ForeignKey(Product,verbose_name="Product", on_delete=models.SET_NULL, null=True, blank=True)
    unit_price = models.DecimalField(max_digits=6,verbose_name="Price", decimal_places=2)
    qty = models.PositiveIntegerField(default=0, verbose_name="Qty",null=True)
    total_price = models.DecimalField(max_digits=10,verbose_name="Total price", decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
