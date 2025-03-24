from django.urls import path
from . import views

urlpatterns = [
    path('compra_venda/', views.track, name='track'),
    path('dog/', views.view_logs, name='view_logs'),
]