from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
	path('about/', about, name='about'),
	path('gallery/', gallery, name='gallery'),

]