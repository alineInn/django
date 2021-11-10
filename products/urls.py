from django.urls import path
from .views import home, form, create, view

urlpatterns = [
    path('', home, name='home'),
    path('form/', form),
    path('create/', create, name='create'),
    path('view/', view, name='view'),


]