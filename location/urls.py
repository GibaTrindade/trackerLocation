from django.urls import path
from . import views

urlpatterns = [
    path('track/', views.track, name='track'),
    path('logs/', views.view_logs, name='view_logs'),
]