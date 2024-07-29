from django.shortcuts import render
from firebase_admin import storage
from datetime import timedelta
from gallery.models import Image

def index(request):
    return render(request, 'gallery/index.html')

# def image_gallery(request):
#     images = Image.objects.all()
#     return render(request, 'gallery/media.html', {'images': images})

def image_gallery(request):
    bucket = storage.bucket()
    blobs = bucket.list_blobs()
    images = []

    for blob in blobs:
        if blob.content_type.startswith('image/'):
            image_url = blob.generate_signed_url(timedelta(seconds=300), method='GET')
            images.append({'image_url': image_url})

    return render(request, 'gallery/media.html', {'images': images})
