from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from .models import *
admin.site.unregister(Group)

@admin.register(Bachelor)
class BachelorAdmin(UserAdmin):
    pass

class GameAdmin(admin.StackedInline):
    model = Game

@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    inlines = [GameAdmin]
    list_display = ['__str__', 'when', 'where', 'organizer', 'nr_of_guests']
