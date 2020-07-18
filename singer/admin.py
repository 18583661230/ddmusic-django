from django.contrib import admin
from .models import Singer,SingerInfo
# Register your models here.


class SingerInfoInline(admin.TabularInline):
    model = SingerInfo
class SingerManger(admin.ModelAdmin):
    inlines = [SingerInfoInline]
    fieldsets = ( ['Main',{
            'fields':('id','name','is_team'),
        }],
        ['Advance',{
            'classes': ('collapse',), # CSS
            'fields': ('area','lable_set','introduce'),
        }])

admin.site.register(Singer,SingerManger)
admin.site.register(SingerInfo)