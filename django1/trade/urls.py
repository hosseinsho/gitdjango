from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.submit_product,name = 'submit_product'),
    ]
