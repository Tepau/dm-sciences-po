from django.db import models
from django_countries.fields import CountryField
import datetime


class Brand(models.Model):
    name = models.CharField(max_length=200, unique=True)
    founder = models.CharField(max_length=200)
    country = CountryField()

    def __str__(self):
        return self.name


def create_choice_storage(i):
    my_list = []
    while i <= 512:
        my_list.append((str(i) + 'Go', str(i) + 'Go'))
        i *= 2
    return my_list


class Tablets(models.Model):
    name = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    storage_size = models.CharField(choices=create_choice_storage(4), max_length=10)
    release_year = models.IntegerField(choices=[(i, i) for i in range(1990, datetime.date.today().year + 1)])

    def __str__(self):
        return self.name

