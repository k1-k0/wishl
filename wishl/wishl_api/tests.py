from django.test import TestCase

from .models import Wish, Tag, Image, Moneybox, Shop


class WishTestCase(TestCase):
    def test_wish(self):
        self.assertEquals(
            Wish.objects.count(),
            0
        )

        ray_ban = Shop(name='Ray Ban', address='Moscow')
        ray_ban.save()

        tag_glasses = Tag(name="accessories")
        tag_glasses.save()

        m_glasses = Moneybox(10000)
        m_glasses.save()

        img = Image(url='google.com')
        img.save()

        wish_1 = Wish(
            name='glasses', description='Ray Ban', money=m_glasses, shop=ray_ban, image=img
        )
        wish_1.save()
        wish_1.tags.add(tag_glasses)
        wish_1.save()


        re_store = Shop(name='Re:store', address='SPB')
        re_store.save()

        m_laptop = Moneybox(200000)
        m_laptop.save()

        img_1 = Image(url='google.com')
        img_1.save()

        macbook = Wish(
            name='laptop', description='Macbook Pro 16 2020', money=m_laptop, shop=re_store, image=img_1
        )
        macbook.save()

        tag_comp = Tag(name="computers")
        tag_comp.save()

        macbook.tags.add(tag_comp)
        macbook.save()

        self.assertEquals(
            Wish.objects.count(),
            2
        )

        tag_laptop = Tag(name='laptop')
        tag_laptop.save()

        macbook.tags.add(tag_laptop)
        macbook.save()

        self.assertEquals(
            macbook.tags.all().count(),
            2
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

        Image.objects.create(url='dropbox: my_image')
        Image.objects.create(url='dropbox: my_another_image')

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
        Moneybox.objects.create(goal=100000, balance=0)
        Moneybox.objects.create(goal=1000000, balance=0)

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
            moneybox.residue(),
            90000
        )

        moneybox.push(90000)

        self.assertEquals(
            moneybox.balance,
            100000
        )

        self.assertAlmostEquals(
            moneybox.residue(),
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

