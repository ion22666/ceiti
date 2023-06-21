from django.contrib import admin

from .models import Apartament, Agent

admin.site.register([Apartament, Agent])
