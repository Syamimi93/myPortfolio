from django.urls import path
from mimisite.views import *
 
urlpatterns = [
    path('', index, name='index'),
    path('', portfolio, name='portfolio'),
    path('contact', contact, name='contact'),
]