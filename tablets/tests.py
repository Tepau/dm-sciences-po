from django.test import TestCase
from django.urls import reverse

from .models import Tablets, Brand


class ListPageTestCase(TestCase):

    def setUp(self):
        self.my_brand = Brand.objects.create(name='Brand Name', founder='Founder Name', country='FR')
        self.my_tablet = Tablets.objects.create(name='New Tablet', brand=self.my_brand, storage_size='32Go', release_year='2018')

    def test_list_page(self):
        response = self.client.get(reverse('tablets',))
        name = self.my_tablet.name
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, name)


class DetailPageTestCase(TestCase):

    # test that detail page returns a 200 if the item exists.
    def test_detail_page_returns_200(self):
        my_brand = Brand.objects.create(name='Brand Name', founder='Founder Name', country='FR')
        my_tablet = Tablets.objects.create(name='New Tablet', brand=my_brand, storage_size='32Go', release_year='2018')
        response = self.client.get(reverse('detailTablet', args=(my_tablet.pk,)))
        self.assertEqual(response.status_code, 200)

    # test that detail page returns a 404 if the item doesn't exists.
    def test_detail_page_returns_404(self):
        my_brand = Brand.objects.create(name='Brand Name', founder='Founder Name', country='FR')
        my_tablet = Tablets.objects.create(name='New Tablet', brand=my_brand, storage_size='32Go', release_year='2018')
        response = self.client.get(reverse('detailTablet', args=(my_tablet.pk + 1,)))
        self.assertEqual(response.status_code, 404)


class BrandTestCase(TestCase):

    # test that a new brand is create
    def test_new_brand_is_registered(self):
        old_brands = Brand.objects.count() # count brands before a request
        response = self.client.post(reverse('new',), {
            'name': 'Brand Name',
            'founder': 'Founder Name',
            'country': 'FR',
        })
        new_brands = Brand.objects.count()
        self.assertEqual(new_brands, old_brands + 1)


class TabletTestCase(TestCase):

    # test that a new tablet is create
    def test_new_brand_is_registered(self):
        my_brand = Brand.objects.create(name='Brand Name', founder='Founder Name', country='FR')
        old_tablets = Tablets.objects.count() # count tablets before a request
        response = self.client.post(reverse('newTablet',), {
            'name': 'Tablet Name',
            'brand': my_brand.id,
            'storage_size': '32Go',
            'release_year': '2018',
        })
        new_tablets = Tablets.objects.count()
        self.assertEqual(new_tablets, old_tablets + 1)