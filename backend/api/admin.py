""" This script is the admin page of the program."""
from django.contrib import admin
from .models import Note, Player

admin.site.register(Player)
admin.site.register(Note)