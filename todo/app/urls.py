from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('delete/<str:pk>/', delete, name='delete'),
    path('update/<str:pk>/', update, name='update'),
]
