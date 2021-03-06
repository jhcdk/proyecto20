from unicodedata import name
from django.contrib import admin
from .models import Link


class LinkAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='Personal').exists():
            return ('key', 'name')
        else: 
            return()

admin.site.register(Link, LinkAdmin)    
