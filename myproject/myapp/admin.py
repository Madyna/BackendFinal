from django.contrib import admin
from .models import *

admin.site.register(Products)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Basket)
admin.site.register(BasketItem)
admin.site.register(Delivery)
