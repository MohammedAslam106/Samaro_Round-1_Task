from django.db import models

# Create your models here.

class Product(models.Model):
    title=models.TextField()
    description=models.TextField()
    category=models.TextField()
    image=models.TextField()
    rating=models.JSONField()
    price=models.FloatField()

    def __str__(self):
        return self.title


class Transactions(models.Model):
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    transaction_amount=models.FloatField()
    payment_status=models.BooleanField(default=False)
    transaction_id=models.TextField(unique=True,default='',null=False)

    def __str__(self):
        return self.product_id