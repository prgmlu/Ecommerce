# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'img',
        'category',
        'price',
        'img1',
        'img2',
        'img3',
    )
    list_filter = (
        'category',
        'id',
        'name',
        'img',
        'category',
        'price',
        'img1',
        'img2',
        'img3',
    )
    search_fields = ('name',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Category, CategoryAdmin)
_register(models.Product, ProductAdmin)
