from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.signup),
    path('signup/add',views.adduser),
    path('login/',views.login),
    path('',views.homepage)
    ]
