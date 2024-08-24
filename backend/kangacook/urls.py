from django.urls import path
from . import views

urlpatterns = [
  path('recipes/', views.recipes, name='recipes'),
  path('cuisines/', views.cuisines, name='cuisines'),
]