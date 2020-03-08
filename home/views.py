from django.shortcuts import render


def index(request):
    """A view that display an index page"""
    return render(request, "index.html")


def about(request):
    """A view that display the about page"""
    return render(request, "about.html")


def contact(request):
    """A view that display the about page"""
    return render(request, "about.html")
    