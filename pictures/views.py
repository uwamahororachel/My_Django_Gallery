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

def search_by_cat(request):
    title = 'Search'
    if 'image_category' in request.GET and request.GET['image_category']:
        search_term = request.GET.get('image_category')
        found_results = Image.objects.filter(image_category__name=search_term)
        message = f"{search_term}"
        print(search_term)
        print(found_results)

        return render(request, 'search.html',{'title':title,'search_term':search_term,'images': found_results, 'message': message})
    else:
        message = 'You havent searched yet'
        return render(request, 'search.html',{"message": message})

def location_filter(request, image_location):
    locations = Location.objects.all()
    location = Location.get_location_id(image_location)
    images = Image.filter_by_location(image_location)
    title = f'{location} Photos'
    return render(request, 'location.html', {'images':images, 'locations':locations, 'location':location})
