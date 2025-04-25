from django.shortcuts import render, get_object_or_404, redirect
from .models import Event
# Create your views here.



def catalog_view(request):
    events = Event.objects.all()
    return render(request, 'catalog.html', {'events': events})

def event_detail(request, event_id):
    event = request.GET.get(Event, id=event_id)
    return render(request, 'events/events.html', {
        'event': event,
    })