from django.test import TestCase

from .models import Wish, Tag, Image, Moneybox, Shop


class WishTestCase(TestCase):
    def test_wish(self):
        self.assertEquals(
            Wish.objects.count(),
            0
        )

        Wish.objects.create(
            title='glasses', description='Ray Ban', moneybox=Moneybox(10000), shop=Shop('Ray Ban')
        )

        Wish.objects.create(
            title='laptop', description='Macbook Pro 16 2020', moneybox=Moneybox(200000), shop=Shop('Re:store')
        )

        self.assertEquals(
            Wish.objects.count(),
            2
        )

        macbook = Wish.objects.get(id=2)
        macbook.tag = Tag('computers')

        self.assertEquals(
            macbook.tag.name,
            'computers'
        )


class TagTestCase(TestCase):
    def test_tag(self):
        self.assertEquals(
            Tag.objects.count(),
            0
        )

        Tag.objects.create(name='computers')
        Tag.objects.create(name='summer')
        Tag.objects.create(name='self-education')

        self.assertEquals(
            Tag.objects.count(),
            3
        )


class ImageTestCase(TestCase):
    def test_image(self):
        self.assertEquals(
            Image.objects.count(),
            0
        )

        Image.objects.create(path='dropbox: my_image')
        Image.objects.create(path='dropbox: my_another_image')

        self.assertEquals(
            Image.objects.count(),
            2
        )


class MoneyboxTestCase(TestCase):
    def test_moneybox(self):
        self.assertEquals(
            Moneybox.objects.count(),
            0
        )

        Moneybox.objects.create(goal=1000, balance=1000)
        Moneybox.objects.create(goal=10000, balance=10000)
        Moneybox.objects.create(100000)
        Moneybox.objects.create(1000000)

        self.assertEquals(
            Moneybox.objects.count(),
            4
        )

        moneybox = Moneybox.objects.get(id=3)
        self.assertEquals(
            moneybox.goal,
            100000
        )

        self.assertEquals(
            moneybox.balance,
            0
        )

        moneybox.push(10000)

        self.assertEquals(
            moneybox.balance,
            10000
        )

        self.assertEquals(
            moneybox.is_complete(),
            False
        )

        self.assertAlmostEquals(
            moneybox.residue,
            90000
        )

        moneybox.push(90000)

        self.assertEquals(
            moneybox.balance,
            100000
        )

        self.assertAlmostEquals(
            moneybox.residue,
            0
        )

        self.assertEquals(
            moneybox.is_complete(),
            True
        )


class ShopTestCase(TestCase):
    def test_shop(self):
        self.assertEquals(
            Shop.objects.count(),
            0
        )

        Shop.objects.create(name='Re:store', address='Moscow, Petrovka Ulitsa, 19')
        Shop.objects.create(name='Ray Ban')

        self.assertEquals(
            Shop.objects.count(),
            2
        )

        ray_ban = Shop.objects.get(id=2)

        test_address = 'Petrovka Ulitsa, 2, Moscow'
        ray_ban.address = test_address

        self.assertEquals(
            ray_ban.address,
            'Petrovka Ulitsa, 2, Moscow'
        )

