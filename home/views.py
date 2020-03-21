from django.shortcuts import render
from django.contrib import messages
from home.forms import ContactForm


def index(request):
    """A view that display an index page"""
    return render(request, "index.html")


def about(request):
    """A view that display the about page"""
    return render(request, "about.html")


def portfolio(request):
    """A view that displays a portfolio grid of my work."""
    return render(request, "portfolio.html")


def contact(request):
    """A view that display the contact page and POST form if filled out"""
    contact_class = ContactForm

    return render(request, 'contact.html', {
        'contact_form': contact_class,
    })
