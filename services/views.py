from django.shortcuts import render, get_object_or_404
from .models import Service, ServiceDetails, ServiceCategory


# Create your views here.
def all_services(request):
    services = Service.objects.all()
    return render(request, "services.html", {"services": services})


def service_detail_view(request, service_id):
    service = get_object_or_404(ServiceDetails, id=service_id)
    return render(request, "service-form.html", {"service": service})
