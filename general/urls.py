from django.urls import path
from . import views

app_name = 'general'
urlpatterns = [
    path('', views.general, name='general')
]