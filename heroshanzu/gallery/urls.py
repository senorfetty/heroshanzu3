from django.urls import path
from .views import index, image_gallery

urlpatterns = [
    path('', index, name='index'),
    path('gallery/', image_gallery, name='gallery'),
   
]
