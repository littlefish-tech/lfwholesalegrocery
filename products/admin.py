from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'productname', 'is_published',
                    'price', 'list_date', 'salesmanager')
    list_display_links = ('id', 'productname')

    list_filter = ('salesmanager',)
    list_editable = ('is_published',)
    search_fields = ('productname', 'description',
                     'origin', 'category', 'price')
    list_per_page = 25


admin.site.register(Product, ProductAdmin)
