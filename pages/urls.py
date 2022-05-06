from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage),

    path('company/', views.company),

    path('notices/', views.notices),

    path('services/', views.services),
]