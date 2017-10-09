from django.contrib import admin
from .models import State, District, Tehsil, GramPanchayat, Person
# Register your models here.
admin.site.register(State)
admin.site.register(District)
admin.site.register(Tehsil)
admin.site.register(GramPanchayat)
admin.site.register(Person)
