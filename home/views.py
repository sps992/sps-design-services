from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm


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
    """A view that displays my contact page."""
    return render(request, "contact.html")
