from django.test import TestCase
from rest_framework.test import APIClient
from .models import Product
# Create your tests here.
class ProductTestCase(TestCase):

    def setUp(self):
            self.client = APIClient()

    def test_product_list_empty(self):
        response = self.client.get("/api/products/")
        self.assertEqual(response.data,[])
        self.assertEqual(response.status_code,200)

    def test_product_creation(self):
        data = {
        "name": "Parle G",
        "cost_price": 6,
        "selling_price": 10,
        "stock_quantity": 150,
        }

        response = self.client.post("/api/products/",data,format='json')
        self.assertEqual(response.status_code,201)
        self.assertEqual(Product.objects.count(),1)

    def test_get_product(self):
         data = {
         "name": "Parle G",
         "cost_price": 6,
         "selling_price": 10,
         "stock_quantity": 150,
         }
         product = Product.objects.create(**data)
         response = self.client.get(f"/api/products/{product.pk}/")
         self.assertEqual(response.status_code,200)
         self.assertEqual(response.data["name"],"Parle G")

    def test_product_update(self):
        product = Product.objects.create(
            name="Parle G",
            cost_price=6,
            selling_price=10,
            stock_quantity=150,
        )

        data = {
            "name": "Parle G Family Pack",
            "cost_price": 8,
            "selling_price": 15,
            "stock_quantity": 100,
        }

        response = self.client.put(
            f"/api/products/{product.pk}/",
            data,
            format="json"
        )

        self.assertEqual(response.status_code, 200)

        product.refresh_from_db()

        self.assertEqual(product.name, "Parle G Family Pack")
        self.assertEqual(product.stock_quantity, 100)


    def test_product_partial_update(self):
        product = Product.objects.create(
            name="Parle G",
            cost_price=6,
            selling_price=10,
            stock_quantity=150,
        )

        response = self.client.patch(
            f"/api/products/{product.pk}/",
            {"stock_quantity": 100},
            format="json"
        )

        self.assertEqual(response.status_code, 200)

        product.refresh_from_db()

        self.assertEqual(product.stock_quantity, 100)
        self.assertEqual(product.name, "Parle G")


    def test_product_delete(self):
        product = Product.objects.create(
            name="Parle G",
            cost_price=6,
            selling_price=10,
            stock_quantity=150,
        )

        response = self.client.delete(
            f"/api/products/{product.pk}/"
        )

        self.assertEqual(response.status_code, 204)
        self.assertEqual(Product.objects.count(), 0)