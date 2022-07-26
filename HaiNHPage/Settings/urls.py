from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeSetting, name='settings'),
    path('addCommercial', views.addCommercial, name='addCommercial'),
]
