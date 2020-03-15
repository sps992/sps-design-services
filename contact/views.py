from django.shortcuts import render

# Create your views here.


def contact_form(request):
    """A view that submits a contact form"""
     if request.method == 'POST':
        user_form = userContactForm(request.POST)
        user = auth.authenticate(request.POST['username'],
                                     password=request.POST['password'])