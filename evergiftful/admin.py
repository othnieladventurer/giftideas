from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.template import loader

from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(Subcategory)
admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(ProductImage)


admin.site.register(Wishlist)



admin.site.register(BlogPost)




