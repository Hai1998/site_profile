from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeSetting, name='settings'),
    path('addCommercial/', views.addCommercial, name='addCommercial'),
    path('addCommercial/addRecordCommercial/', views.addRecordCommercial, name='addRecordCommercial'),
    path('updateCommercial/<int:id>', views.updateCommercial, name='updateCommercial'),
    path('updateCommercial/updateRecordCommercial/<int:id>', views.updateRecordCommercial, name='updateRecordCommercial'),
    path('deleteCommercial/<int:id>', views.deleteCommercial, name='deleteCommercial'),
]
