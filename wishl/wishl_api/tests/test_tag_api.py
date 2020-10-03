from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from ..models.tag import Tag


class TagTests(APITestCase):
    """
    Class for testing accessing to Tag API
    """
    def setUp(self):
        """
        Prepare test data
        """
        self.tag_1 = Tag.objects.create(name='computers')
        self.tag_2 = Tag.objects.create(name='location')

        self.user = User.objects.create_user(username='test_u', password='secret1')
        self.client.login(username='test_u', password='secret1')

    def test_create_tag(self):
        """
        Ensure that user can create own tag
        """
        url = reverse('tag-list')
        data = {'name': 'car'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tag.objects.count(), 3)

    def test_edit_tag_name(self):
        """
        Ensure that user can edit tag name
        """
        tag = Tag.objects.first()
        url = f'/tags/{tag.id}/'
        data = {'name': 'cars'}
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Tag.objects.get(id=tag.id).name, 'cars')
        self.assertEqual(Tag.objects.count(), 2)

    def test_remove_tag(self):
        """
        Ensure that user can remove tag
        """
        tag = Tag.objects.first()
        url = f'/tags/{tag.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Tag.objects.count(), 1)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
