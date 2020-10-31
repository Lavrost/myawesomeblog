from django.shortcuts import render
from .models import Event


def home(request):
    events = Event.event_manager.all()
    return render(request, 'events/home.html', {'events': events})
