from django import login
from django.shortcuts import render

from.models import Room

@ login_required
def rooms(request):
    rooms = Room.objects.all

