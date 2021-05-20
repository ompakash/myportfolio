from django.urls import path 
from . import views

urlpatterns = [
    path('om/',views.index,name='index')
]


