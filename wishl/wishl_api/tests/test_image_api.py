from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from rest_framework.test import force_authenticate
from django.contrib.auth.models import User
from ..models.image import Image
from ..views import ImageViewSet


class ImageTests(APITestCase):


    def test_create_image_unauthorized(self):
        """
        Ensure that unauthorized user can't create image
        """
        url = reverse('image-list')
        data = {'url': 'https://www.google.com/'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Image.objects.count(), 0)

    def test_create_image(self):
        """
        Ensure that user can create image
        """

        user = User.objects.create_user(username='test_u', password='secret1')
        self.client.login(username='test_u', password='secret1')

        url = reverse('image-list')
        data = {'url': 'https://www.google.com/'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Image.objects.count(), 1)

    def test_edit_image_url(self):
        pass

    def test_remove_image(self):
        pass