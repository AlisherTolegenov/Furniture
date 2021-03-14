from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name = 'main'),
    path('articles', views.index, name='shop'),
    path('about', views.about, name='about-us'),
    path('contact', views.contact, name='contact-us')
]