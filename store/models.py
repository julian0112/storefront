from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    
class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
    
    MEMBERSHIP_CHOICES = [
        ('MEMBERSHIP_BRONZE', 'Bronze'),
        ('MEMBERSHIP_SILVER', 'Silver'),
        ('MEMBERSHIP_GOLD', 'Gold')
    ]
    
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)
    
class Order(models.Model):
    PENDING_PAYMENT_STATUS = 'P'
    COMPLETE_PAYMENT_STATUS = 'C'
    FAILED_PAYMENT_STATUS = 'F'
    
    PAYMENT_STATUS_CHOICES = [
        (PENDING_PAYMENT_STATUS, 'Pending'),
        (COMPLETE_PAYMENT_STATUS, 'Complete'),
        (FAILED_PAYMENT_STATUS, 'Failed')
    ]
    
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PENDING_PAYMENT_STATUS)
    