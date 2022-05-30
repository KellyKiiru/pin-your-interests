from django.test import TestCase
from .models import category, Location,Pin

# Create your tests here.
class Testcategory(TestCase):
    def setUp(self):
        self.category_trial = category(category_name="category trial")

    def test_category_instance(self):
        self.assertTrue(isinstance(self.category_trial, category))

class TestLocation(TestCase):
    def setUp(self) -> None:
        self.location_trial = Location(location="Cote d'ivoire")

    def test_location_instance(self):
        self.assertTrue(isinstance(self.location_trial, Location))
