from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from ..models.image import Image


class ImageTests(APITestCase):
    """
    Class for testing accessing to Image API
    """
    def setUp(self):
        """
        Prepare test data
        """
        self.image_1 = Image.objects.create(url='https://www.google.com/')
        self.image_2 = Image.objects.create(url='https://www.facebook.com/')

        self.user = User.objects.create_user(username='test_u', password='secret1')
        self.client.login(username='test_u', password='secret1')

    def test_create_image(self):
        """
        Ensure that user can create image
        """
        url = reverse('image-list')
        data = {'url': 'https://www.gg.com/'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Image.objects.count(), 3)

    def test_edit_image_url(self):
        """
        Ensure that user can edit image
        """
        image = Image.objects.last()
        url = f'/images/{image.id}/'
        data = {'url': 'https://www.fff.com/'}
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Image.objects.get(id=image.id).url, 'https://www.fff.com/')
        self.assertEqual(Image.objects.count(), 2)

    def test_remove_image(self):
        """
        Ensure that user can remove image
        """
        image = Image.objects.first()
        url = f'/images/{image.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Image.objects.count(), 1)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
