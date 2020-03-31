from django.contrib import admin
from .models import Service, ServiceCategory, ServiceDetails

# Register your models here.
admin.site.register(Service)

admin.site.register(ServiceCategory)

admin.site.register(ServiceDetails)
