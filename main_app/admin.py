from django.contrib import admin


# Register your models here.
from .models import Package, Profile
admin.site.register(Package)
admin.site.register(Profile)
