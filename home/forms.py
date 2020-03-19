from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=25, blank=False)
    last_name = forms.CharField(max_length=25, blank=False)
    email = forms.EmailField(blank=False)
    subject = forms.CharField(max_length=25, blank=False)
    message = forms.TextField(max_length=500, default='')



