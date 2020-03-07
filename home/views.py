from django.shortcuts import render


def index(request):
    """A view that display an index page"""
    return render(request, "index.html")
    