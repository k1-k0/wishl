from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from ..models.wish import Wish
from ..models.moneybox import Moneybox
from ..models.shop import Shop
from ..models.image import Image
from ..models.tag import Tag


class WishTests(APITestCase):
    """
    Class for testing accessing to Wish API
    """
    def setUp(self):
        """
        Prepare test data
        """
        self.user = User.objects.create_user(username='test_u', password='secret1')

        self.moneybox_1 = Moneybox.objects.create(goal=80000)
        self.moneybox_2 = Moneybox.objects.create(goal=200000)
        self.moneybox_3 = Moneybox.objects.create(goal=20000, balance=2000)
        self.moneybox_4 = Moneybox.objects.create(goal=500)

        self.shop_1 = Shop.objects.create(name="Lenovo")
        self.shop_2 = Shop.objects.create(name="re:store", address='Красная площадь 3, ТД ГУМ, Moscow, 109012')
        self.shop_4 = Shop.objects.create(name="Moscow Zoo", address='Bolshaya Gruzinskaya St, 1, Moscow, 123242')
        self.shop_5 = Shop.objects.create(name="Levi's")

        self.tag_1 = Tag.objects.create(name='computers')
        self.tag_2 = Tag.objects.create(name='study')
        self.tag_3 = Tag.objects.create(name='location')
        self.tag_4 = Tag.objects.create(name='fun')
        self.tag_5 = Tag.objects.create(name='extreme')

        self.image_1 = Image.objects.create(
            url='https://static.bhphoto.com/images/images500x500/1590507975_1566271.jpg'
            )
        self.image_2 = Image.objects.create(
            url='https://www.apple.com/v/macbook-pro-16/b/images/meta/og__csakh451i0eq_large.png'
            )

        # Nominal wish(w/ all fields)
        self.wish_1 = Wish.objects.create(
            user=self.user,
            title='Laptop for college',
            description='Hello all! I need a laptop to study, as most practical work takes place at lectures',
            money=self.moneybox_1,
            shop=self.shop_1,
            image=self.image_1
            )
        self.wish_1.tags.add(self.tag_1, self.tag_2)

        # Wish w/o description
        self.wish_2 = Wish.objects.create(
            user=self.user,
            title='Laptop for fun',
            money=self.moneybox_2,
            shop=self.shop_2,
            image=self.image_2
            )
        self.wish_2.tags.add(self.tag_1, self.tag_4)

        # Wish w/o description, shop, image
        self.wish_3 = Wish.objects.create(
            user=self.user,
            title='Bungee jump',
            money=self.moneybox_3
            )
        self.wish_3.tags.add(self.tag_4, self.tag_5)

        # Wish w/o description, shop, image, tags
        self.wish_4 = Wish.objects.create(
            user=self.user,
            title='Icecream',
            description='',
            money=self.moneybox_4
            )

        self.client.login(username='test_u', password='secret1')

    def test_create_wish(self):
        """
        Ensure that user can create own wish
        """
        self.car_money = Moneybox.objects.create(balance=20000, goal=1500000)

        url = reverse('wish-list')
        data = {
            'user': self.user.id,
            'title': 'Audi A5',
            'description': '',
            'money': self.car_money.id
            }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Wish.objects.count(), 5)

    def test_edit_wish_title(self):
        """
        Ensure that user can edit wish name
        """
        wish = Wish.objects.first()
        url = f'/wishes/{wish.id}/'
        data = {
            'user': wish.user.id,
            'title': wish.title + "(funny)",
            'description': wish.description,
            'money': wish.money.id,
            'shop': wish.shop.id,
            'tags': [tag.id for tag in wish.tags.all()]
            }
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Wish.objects.get(id=wish.id).title, wish.title+"(funny)")
        self.assertEqual(Wish.objects.count(), 4)

    def test_remove_wish(self):
        """
        Ensure that user can remove wish
        """
        wish = Wish.objects.last()
        url = f'/wishes/{wish.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Wish.objects.count(), 3)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
