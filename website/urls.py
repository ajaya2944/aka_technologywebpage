from django.urls import path
from .views import home, about, service, gallery, contact,contact_success
from . import views


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('service/', service, name='service'),
    path('gallery/', gallery, name='gallery'),
    path('contact/', contact, name='contact'),
    path('contact-success/', views.contact_success, name='contact_success'),
]
