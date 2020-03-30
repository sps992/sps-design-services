from django.shortcuts import render, get_object_or_404
from .models import Service, ServiceDetails, ServiceCategory


# Create your views here.
def all_services(request):
    #services = Service.objects.filter(category__category_name='Basic')
    services = Service.objects.filter(category__category_name__icontains='Basic')
    return render(request, "services.html", {"services": services})


def service_detail_view(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    services = Service.objects.filter(name__iexact=service.name)
    return render(request, 'service-form.html', {'services': services})
