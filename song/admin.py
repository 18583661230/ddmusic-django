from .models import Song
from django.contrib import admin
# Register your models here.




class SongManager(admin.ModelAdmin):
    list_display = ['name', 'singer', 'is_active']


admin.site.register(Song, SongManager)
