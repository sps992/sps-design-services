from django.conf.urls import url, include
from .views import all_services, service_detail_view

urlpatterns = [
    url(r'^$', all_services, name='services'),
    #url(r'^service-form/<service_id>', service_detail_view, name='service_detail_view'),
    url(r'^(?P<service_id>\d+)$', service_detail_view, name='service_detail_view'),
    
    
    ]