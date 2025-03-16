"""
URL configuration for logis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('pricing/pay/',views.pay,name='pay'),
    path('contact/', views.contact, name='contact'),
    path('pricing/', views.pricing, name='pricing'),
    path('services/', views.services, name='services'),
    path('services-details/', views.services_details, name='services-details'),
    path('starter-page/', views.starter_page, name='starter-page'),
    path('get-a-quote/', views.get_a_quote, name='get-a-quote'),
    path('contactlist/',views.contactlist, name='contactlist'),
    path('updatecontact/<int:id>/', views.updatecontact, name='updatecontact'),
    path('deletecontact/<int:id>/', views.deletecontact, name='deletecontact'),
    #path('initiate-mpesa-payment/',views.initiate_mpesa_payment,'initiate_mpesa_payment'),
    path('initiate-mpesa-payment/', views.initiate_mpesa_payment),



]
