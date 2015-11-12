from django.contrib import admin

from shortcuts.models import Shortcut, Choices


# Register your models here.
class ShortcutAdmin(admin.ModelAdmin):
    list_display = ('shortcut_cmd',)
    search_fields = ['shortcut_cmd']

    fields = ['shortcut_cmd', 'shortcut_desc']
    
admin.site.register(Shortcut, ShortcutAdmin)


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']
    
    fields = ['name', 'first_key', 'second_key']

admin.site.register(Choices, ChoiceAdmin)