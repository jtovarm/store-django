# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ActivityName(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    date_up = models.DateField(blank=True, null=True)
    image = models.FileField(upload_to=u'upload-product/')

    def as_dict(self):
        _dict = {
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'date_up': self.date_up,
            'image': self.image.url
        }

        return _dict

    def __unicode__(self):
        return self.name

class DataTable:
    def __init__(self, request_data, column_map):
        self.request_data = request_data
        self.column_map = column_map
        self.start = int(request_data.get('start'))
        self.length = int(request_data.get('length'))
        self.draw = request_data.get('draw')
        self.limit = self.start + self.length
        self.search_value = self.request_data.get('search[value]', '')

    def get_column_data(self, i):
        column_data = 'columns[{}][data]'.format(i)
        return self.request_data.get(column_data, False)

    def get_order_direction(self, i):
        order_dir = 'order[{}][dir]'.format(i)
        return self.request_data.get(order_dir, False)

    def get_order_column(self, i):
        order_column = 'order[{}][column]'.format(i)
        return self.request_data.get(order_column, False)

    def get_local_key(self, data_key):
        return self.column_map[data_key]

    def get_orderings(self):
        orderings = []
        for i in range(0, len(self.column_map.keys())):
            order_column = self.get_order_column(i)
            if not order_column:
                break

            order_direction = self.get_order_direction(i)
            if not order_direction:
                break

            column_data = self.get_column_data(order_column)
            if not column_data:
                break

            local_ley = self.get_local_key(column_data)

            p_dir = '' if order_direction == "asc" else '-'
            ordering = '{}{}'.format(p_dir, local_ley)
            orderings.append(ordering)

        return orderings