from django.urls import path
from .views import *

urlpatterns = [
    path('', show_category, name='category'),
]
