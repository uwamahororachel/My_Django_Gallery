from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Image, Location, Category

def gallery(request):
    images = Image.objects.all()
    categories = Category.objects.all()
    locations = Location.objects.all()
    return render(request, 'index.html', {"images":images,"categories":categories,'locations':locations})

def picture(request,category_name,image_id):
    title = 'Image'
    locations = Location.objects.all()
    image_category = Image.objects.filter(image_category__name = category_name)
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"gallery.html",{'title':title,"image":image, "locations":locations, "image_category":image_category})

