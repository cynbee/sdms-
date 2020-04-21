from django.urls import path
from details import views

urlpatterns = [
    path('', views.my_index, name='index'),
    path('detail/', views.my_detail, name='detail'),
    path('contract/', views.my_contract, name='contract')
]
