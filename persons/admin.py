from django.contrib import admin
from .models import City, Country, Person

admin.site.register(Person)
admin.site.register(Country)
admin.site.register(City)