from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    base_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
