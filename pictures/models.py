from django.db import models
import datetime as dt

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length =50)
     
    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category(self, update):
        self.name = update
        self.save()

    @classmethod
    def get_category_id(cls, id):
        category = Category.objects.get(pk = id)
        return category
    
    

class Location(models.Model):
    name = models.CharField(max_length =50)

    def __str__(self):
        return self.name

    @classmethod
    def tag_articles(cls):
        tags = cls.objects.all()
        return tags

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location(self, update):
        self.name = update
        self.save()

    @classmethod
    def get_location_id(cls, id):
        locate = Location.objects.get(pk = id)
        return locate

   

class Image(models.Model):
    image = models.ImageField(upload_to = 'pictures/',null=True)
    image_name = models.CharField(max_length =30)
    image_description = models.TextField()
    image_location = models.ForeignKey(
        'Location',
        on_delete=models.CASCADE,
        )
    image_category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        )

    def __str__(self):
        return self.image_name
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    
    @classmethod
    def update_image(cls, id ,name, description , image_location, image_category):
        update = cls.objects.filter(id = id).update(name = name, description = description ,image_location = image_location,image_category = image_category)

    @classmethod
    def get_image_by_id(id):
        image = cls.objects.filter(id=id)
        return image

    @classmethod
    def search_image(cls,category):
        pictures = cls.objects.filter(image_category__name__icontains=category)
        return pictures

    @classmethod
    def filter_by_location(cls,location):
        pictures = cls.objects.filter(image_location=location)
        return pictures

    class Meta:
        ordering = ['image_name']
