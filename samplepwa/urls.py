from . import views
from django.urls import path

app_name = 'samplepwa'

urlpatterns = [

    path('', views.index, name='index'),

]
