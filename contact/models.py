from django.db import models

# Create your models here.
class ContactForm(models.Model):
    first_name = models.CharField(max_length=25, blank=False)
    last_name = models.CharField(max_length=25, blank=False)
    email = models.EmailField(blank=False)
    subject = models.CharField(max_length=25, blank=False)
    message = models.TextField(max_length=500, default='')
    