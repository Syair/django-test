from django.urls import path
from . import views

app_name = 'loadMeta'
urlpatterns = [
    path('', views.index, name='index'),
    path('load', views.load, name='load')
]