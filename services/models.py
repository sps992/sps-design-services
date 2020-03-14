from django.db import models


class ServiceCategory(models.Model):
    """To define the category in which the service falls into (i.e. basic, standard and premium) and gives a price rate"""
    category_name = models.CharField(max_length=254, default='')
    price_rate = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.category_name


class ServiceDetails(models.Model):
    """Model to build variable details in services"""
    delivery_time_choices = (
        (20, "20"),
        (14, "14"),
        (7, "7"),
    )
    amendment_choices = (
        (3, "3"),
        (5, "5"),
        (7, "7"),
    )

    title = models.CharField(max_length=254, default='')
    contents = models.CharField(max_length=254, default='')
    delivery_time = models.IntegerField(choices=delivery_time_choices, default=20)
    ammendments = models.IntegerField(choices=amendment_choices, default=3)
    description = models.TextField(default='')
    #service = models.ForeignKey(Service, on_delete=models.CASCADE)
    #category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Service(models.Model):
    """Model to store services"""
    name = models.CharField(max_length=254, default='')
    image = models.ImageField(upload_to='images')
    base_price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(ServiceCategory,
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL)
    details = models.ForeignKey(ServiceDetails,
                                null=True,
                                blank=True,
                                on_delete=models.SET_NULL)
                                
    def __str__(self):
        return self.name
