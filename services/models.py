from django.db import models


class ServiceCategory(models.Model):
    """To define the category in which the service falls into (i.e. basic, standard and premium) and gives a price rate"""
    category_name = models.CharField(max_length=254, default='')
    plan_image = models.ImageField(upload_to='images', blank=True, null=True)
    price_rate = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.category_name


class ServiceDetails(models.Model):
    """Model to build variable details in services"""
    delivery_time_choices = (
        ("Delivery Time: 30 Days", "30 Days"),
        ("Delivery Time: 28 Days", "28 Days"),
        ("Delivery Time: 21 Days", "21 Days"),
        ("Delivery Time: 14 Days", "14 Days"),
        ("Delivery Time: 7 Days", "7 Days"),
        ("Delivery Time: 3 Days", "3 Days"),
        (" ", " "),
        
    )
    amendment_choices = (
        ("Amendments: 3", "3"),
        ("Amendments: 5", "5"),
        ("Amendments: 7", "7"),
        ("Amendments: UNLIMITED", "UNLIMITED"),
        (" ", " "),
        
    )

    title = models.CharField(max_length=254, default=' ')
    contents = models.CharField(max_length=254, default=' ')
    delivery_time = models.CharField(choices=delivery_time_choices, default='', max_length=254, blank=True, null=True)
    amendments = models.CharField(choices=amendment_choices, default='', max_length=254, blank=True, null=True)
    description = models.TextField(default='')

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
