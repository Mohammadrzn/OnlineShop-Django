from django.test import TestCase
from .models import Category, Product, Comment


class CategoryTest(TestCase):

    def setUp(self) -> None:
        self.product = Product.objects.create(name="test", price=150.5, count=5, brand="test", description="test",
                                              is_sold_out=False)
        self.category = Category.objects.create(name="test")
        self.comment = Comment.objects.create(title="test", content="test & test")

    def test_create_product(self):
        self.assertEqual(self.product.name, "test")
        self.assertEqual(self.product.price, 150.5)
        self.assertEqual(self.product.count, 5)
        self.assertEqual(self.product.brand, "test")
        self.assertEqual(self.product.description, "test")
        self.assertEqual(self.product.is_sold_out, False)

    def test_create_category(self):
        self.assertEqual(self.category.name, "test")
        self.assertFalse(self.category.is_deleted)

    def test_create_comment(self):
        self.assertEqual(self.product.title, "test")
        self.assertEqual(self.product.content, "test & test")
