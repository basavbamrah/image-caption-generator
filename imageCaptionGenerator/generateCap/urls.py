from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='generateCap'),
    path('generate/', views.generate, name='generate'),
] 
