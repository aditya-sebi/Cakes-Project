from io import BytesIO

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from PIL import Image
from rest_framework.test import APIClient

from .models import Cakes, Category, Shape, Weight


class CakeApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = Category.objects.create(name='Birthday cake')
        self.shape = Shape.objects.create(name='Round')
        self.weight = Weight.objects.create(name='1 kg')

    def test_shape_list_and_retrieve(self):
        response = self.client.get('/shapes/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [{'id': self.shape.id, 'name': 'Round'}])

        response = self.client.get(f'/shapes/{self.shape.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'id': self.shape.id, 'name': 'Round'})

    def test_shape_retrieve_returns_404_for_missing_shape(self):
        response = self.client.get('/shapes/999/')
        self.assertEqual(response.status_code, 404)

    def test_cake_create_and_update_with_related_ids(self):
        admin = get_user_model().objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='test-password',
        )
        self.client.force_authenticate(user=admin)
        image_buffer = BytesIO()
        Image.new('RGB', (1, 1)).save(image_buffer, format='PNG')
        image = SimpleUploadedFile(
            'cake.png',
            image_buffer.getvalue(),
            content_type='image/png',
        )
        response = self.client.post(
            '/cakes/',
            {
                'name': 'Chocolate Cake',
                'description': 'Rich chocolate cake',
                'photo': image,
                'category_id': self.category.id,
                'shape_id': self.shape.id,
                'weight_id': self.weight.id,
                'price': 1000,
            },
            format='multipart',
        )
        self.assertEqual(response.status_code, 201, response.data)

        cake = Cakes.objects.get(name='Chocolate Cake')
        response = self.client.patch(
            f'/cakes/{cake.id}/',
            {'price': 1500},
            format='json',
        )
        self.assertEqual(response.status_code, 200, response.data)
        cake.refresh_from_db()
        self.assertEqual(cake.price, 1500)

    def test_cake_retrieve_returns_404_for_missing_cake(self):
        response = self.client.get('/cakes/999/')
        self.assertEqual(response.status_code, 404)
