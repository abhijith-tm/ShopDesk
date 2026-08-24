from django.test import TestCase

from products.models import Product
from sales.models import Sale, SaleItem
from sales.services import create_sale
from rest_framework.exceptions import ValidationError


class CreateSaleTests(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="Parle G",
            cost_price=7,
            selling_price=10,
            stock_quantity=10,
        )

    def test_create_sale(self):
        data = {
            "items": [
                {
                    "product_id": self.product,
                    "quantity": 3,
                }
            ]
        }

        sale = create_sale(data)

        self.assertEqual(sale.status, "completed")
        self.assertEqual(Sale.objects.count(), 1)
        self.assertEqual(SaleItem.objects.count(), 1)

    def test_create_sale_low_stock(self):
        data = {
            "items": [
                {
                    "product_id": self.product,
                    "quantity": 15,
                }
            ]
        }

        with self.assertRaises(ValidationError):
            sale = create_sale(data)

        self.product.refresh_from_db()

        self.assertEqual(Sale.objects.count(), 0)
        self.assertEqual(SaleItem.objects.count(), 0)
        self.assertEqual(self.product.stock_quantity, 10)

    def test_create_sale_with_multiple_items(self):
        data = {
            "items": [
                {
                    "product_id": self.product,
                    "quantity": 1,
                },
        {
                    "product_id": self.product,
                    "quantity": 2,
                },
         {
                    "product_id": self.product,
                    "quantity": 3,
                }
            ]
         }

        sale = create_sale(data)
        
        self.assertEqual(Sale.objects.count(), 1)
        self.assertEqual(SaleItem.objects.count(), 3)
        self.assertEqual(self.product.stock_quantity, 4)

    def test_sale_item_keeps_historical_snapshot(self):
        data = {
            "items": [
                {
                    "product_id": self.product,
                    "quantity": 2,
                }
            ]
        }

        sale = create_sale(data)

        self.product.name = "Changed Name"
        self.product.selling_price = 20
        self.product.cost_price = 15
        self.product.save()

        item = sale.items.first()

        self.assertEqual(item.product_name, "Parle G")#name Parle G shouldnt change
        self.assertEqual(item.unit_price, 10)
        self.assertEqual(item.cost_price, 7)