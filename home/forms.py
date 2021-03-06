from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=25, required=True)
    last_name = forms.CharField(max_length=25, required=True)
    email_address = forms.EmailField(required=True)
    subject = forms.CharField(max_length=25, required=True)
    message = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
