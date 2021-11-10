from django.urls import path
from .views import home, create, view

urlpatterns = [
    path('', home, name='home'),
    path('create/', create, name='create'),
    path('view/<int:pk>', view, name='view'),


]