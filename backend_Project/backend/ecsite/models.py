from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.


class Ecsite(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title
    
class Users(AbstractBaseUser):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    
    phone = models.CharField(max_length=120)
    ship_number = models.CharField(max_length=120)
    address = models.CharField(max_length=120)

    register_date =  models.DateTimeField(help_text='作成日')
    order_date = models.DateTimeField(help_text='注文日')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name_plural = 'ユーザ情報'


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateTimeField()
    order_status = models.CharField(max_length=50)
    
    recipient_name = models.CharField(max_length=100)
    recipient_address = models.CharField(max_length=200)
    recipient_phone = models.CharField(max_length=20)
    recipient_email = models.EmailField()

    customer_name = models.CharField(max_length=100)
    customer_address = models.CharField(max_length=200)
    customer_phone = models.CharField(max_length=20)
    customer_email = models.EmailField()
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='orders')

    def __str__(self):
        return f'Order #{self.order_id}'
    

class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    totalprice = models.DecimalField(max_digits=10, decimal_places=2)


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)


class Category(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True)