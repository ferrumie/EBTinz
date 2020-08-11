from django.contrib import admin
from .models import Tins
# Register your models here.

class TinAdmin(admin.ModelAdmin):
    list_display = ["__str__", "user"]
    search_fields = ['content', 'user__username', 'user__email']
admin.site.register(Tins, TinAdmin)