from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(blank=False, null=False)
    stock = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.8)
    def __str__(self):
        return self.name