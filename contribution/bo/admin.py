from django.contrib import admin
from .models import Medias


class MediaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Medias,MediaAdmin)
