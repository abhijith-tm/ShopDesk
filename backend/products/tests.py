from django.test import TestCase
from rest_framework.test import APIClient


# Create your tests here.
class ProductTestCase(TestCase):

    def setUp(self):
            self.client = APIClient()

    def test_product_list_empty(self):
        response = self.client.get("/api/products/")
        self.assertEqual(response.data,[])
        self.assertEqual(response.status_code,200)

    def test_product_creation(self):
        response = self.client.post("/api/products/", {'name': 'Parle G','cost_price': '6','selling_price': '10','stock_quantity': '150'} ,format='json')
        self.assertEqual(response.data,{'name': 'Parle G''cost_price': '6''selling_price': '10''stock_quantity': 150},format='json')
        self.assertEqual(response.status_code,201)