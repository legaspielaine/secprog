from django.contrib import admin
from .models import Item, Review, User

# Register your models here.
admin.site.register(Item)
admin.site.register(Review)
admin.site.register(User)