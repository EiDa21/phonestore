from django.urls import path
from . import views

app_name = "myphonestore"

urlpatterns = [
   path('', views.home, name='Home'),
   path('about/', views.about, name='about'),
   path('computer/', views.computer, name='computer'),
   path('computer/', views.laptop, name='laptop'),
   path('computer/', views.product, name='product'),
   path('computer/', views.contact, name='contactUs'),

]

