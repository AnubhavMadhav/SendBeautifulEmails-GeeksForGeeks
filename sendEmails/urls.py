from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('staticText', views.staticText, name='staticText'),
    path('dynamicTextHTML', views.dynamicTextHTML, name='dynamicTextHTML'),
    path('beautifulHTMLEmail', views.beautifulHTMLEmail, name='beautifulHTMLEmail'),
    path('attachmentEmail', views.attachmentEmail, name='attachmentEmail'),
]
