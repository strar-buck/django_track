from django.contrib import admin

# Register your models here.
from models import Tracks,Genre

admin.site.register(Tracks)

admin.site.register(Genre)