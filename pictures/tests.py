from django.test import TestCase
from .models import Image,Category,Location

# Create your tests here.
class CategoryTestClass(TestCase):
    def setUp(self):
        self.cat = Category(name="games")
        self.cat.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.cat, Category))

    def test_save_method(self):
        self.cat.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

    def test_delete_method(self):
        self.cat.save_category()
        self.cat.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)

    def test_update(self):
        category = Category.get_category_id(self.cat.id)
        category.update_category('Anime')
        category = Category.get_category_id(self.cat.id)
        self.assertTrue(category.name == 'Anime') 


class LocationTestCLass(TestCase):
    def setUp(self):
        self.loc = Location(name="Kigali")
        self.loc.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.loc,Location))

    def test_delete_method(self):
        self.loc.save_location()
        self.loc.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)

    def test_update(self):
        location = Location.get_location_id(self.loc.id)
        location.update_location('Paris')
        location = Location.get_location_id(self.loc.id)
        self.assertTrue(location.name == 'Paris')


