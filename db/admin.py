from django.contrib import admin
from .models import Team, Publisher, SuperHero
# Register your models here.

admin.site.register(Team)
admin.site.register(Publisher)
admin.site.register(SuperHero)
