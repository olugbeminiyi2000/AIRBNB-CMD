from models.city import City
from models import storage
import unittest


class TestCity(unittest.TestCase):

  def test_city_initialization(self):
    city_1 = City()
    self.assertIsInstance(city_1, City)
    city1_id = city_1.id
    city1_class_name = type(city_1).__name__
    city1_key = f"{city1_class_name}.{city1_id}"
    city_1.save()
    storage.reload()
    self.assertTrue(city1_key in storage.all())
