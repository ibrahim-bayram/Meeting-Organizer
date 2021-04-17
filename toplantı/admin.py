from django.contrib import admin
from .models import Toplantı

class ToplantıAdmin(admin.ModelAdmin):
    list_display = ('id','name','tarih','isPublished')
    list_display_links = ('id','name')
    list_editable = ('isPublished',)
# Register your models here.
admin.site.register(Toplantı, ToplantıAdmin)
