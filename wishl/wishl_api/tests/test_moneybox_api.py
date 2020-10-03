from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from ..models.moneybox import Moneybox


class MoneyboxTests(APITestCase):
    """
    Class for testing accessing to Moneybox API
    """
    def setUp(self):
        """
        Prepare test data
        """
        self.moneybox_1 = Moneybox.objects.create(name='a')
        self.moneybox_2 = Moneybox.objects.create(name='b', goal=10000)
        self.moneybox_3 = Moneybox.objects.create(name='b', goal=100000, balance=50000)

        self.user = User.objects.create_user(username='test_u', password='secret1')
        self.client.login(username='test_u', password='secret1')

    def test_create_moneybox(self):
        """
        Ensure that user can create own moneybox
        """
        url = reverse('moneybox-list')
        data = {'name': 'test', 'goal': 250000}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Moneybox.objects.count(), 4)

    def test_edit_moneybox(self):
        """
        Ensure that user can edit moneybox information
        """
        moneybox = Moneybox.objects.first()
        url = f'/moneyboxes/{moneybox.id}/'
        data = {'name': 'test', 'goal': 200000, 'balance': 25000}
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Moneybox.objects.get(id=moneybox.id).goal, 200000)
        self.assertEqual(Moneybox.objects.get(id=moneybox.id).balance, 25000)
        self.assertEqual(Moneybox.objects.count(), 3)

    def test_remove_moneybox(self):
        """
        Ensure that user can remove moneybox
        """
        moneybox = Moneybox.objects.last()
        url = f'/moneyboxes/{moneybox.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Moneybox.objects.count(), 2)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
