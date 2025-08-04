from django.urls import path
from . import views

app_name = 'certapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('verification', views.verification, name='verification'),
]