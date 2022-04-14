from django.urls import path
from . import views

urlpatterns = [
     path('add_person', views.person, name = "person"),
     path('cities', views.cities, name = "cities")
]
