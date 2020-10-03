from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from ..models.shop import Shop


class ShopTests(APITestCase):
    """
    Class for testing accessing to Shop API
    """
    def setUp(self):
        """
        Prepare test data
        """
        self.shop_1 = Shop.objects.create(name='re:store', address='Красная площадь 3, ТД ГУМ, Moscow, 109012')
        self.shop_2 = Shop.objects.create(name='Moscow Zoo', address='Bolshaya Gruzinskaya St, 1, Moscow, 123242')
        self.shop_3 = Shop.objects.create(name="Levi's")

        self.user = User.objects.create_user(username='test_u', password='secret1')
        self.client.login(username='test_u', password='secret1')

    def test_create_shop(self):
        """
        Ensure that user can create own shop
        """
        url = reverse('shop-list')
        data = {'name': 'Ray Ban', 'address': 'ТЦ "ЦУМ, Petrovka Ulitsa, 2, Moscow, 125009'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Shop.objects.count(), 4)

    def test_edit_shop(self):
        """
        Ensure that user can edit shop information
        """
        shop = Shop.objects.first()
        url = f'/shops/{shop.id}/'
        data = {'name': 'Re:store', 'address':'Красная площадь 3, ТД ГУМ, Moscow, 109012'}
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Shop.objects.get(id=shop.id).name, 'Re:store')
        self.assertEqual(Shop.objects.count(), 3)

    def test_remove_shop(self):
        """
        Ensure that user can remove shop
        """
        shop = Shop.objects.last()
        url = f'/shops/{shop.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Shop.objects.count(), 2)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
