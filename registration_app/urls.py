from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('register/', views.register, name='register'),
    path('success/<str:first_name>/', views.success, name='success'),
]