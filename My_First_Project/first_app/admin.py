from django.contrib import admin

#model import
from first_app.models import Musician, Album


# Register your models here.
admin.site.register(Musician)
admin.site.register(Album)
