from django.db import models




# Create your models here.


class Product(models.Model):
    productname = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    itemsimg =models.ImageField(upload_to="product", null=True)


class Cart(models.Model):
    name=models.ForeignKey(Product, on_delete=models.CASCADE)
    productname = models.CharField
    price = models.DecimalField
    # description = models.TextField()
    def __str__(self):
        return self.name