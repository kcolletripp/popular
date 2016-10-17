from django.contrib import admin

from .models import Target

#class TargetWikiInline(admin.TabularInline):
#    model = TargetWiki
#    extra = 1

class TargetAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['target_name', 'wiki_views']}),
        
    ]
    search_fields = ['target_name']


admin.site.register(Target, TargetAdmin)
#admin.site.register(Choice) #this offers a quick a dirty way of adding it
