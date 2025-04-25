from django.shortcuts import render, get_object_or_404, redirect
from .models import Event
# Create your views here.



def catalog_view(request):
    events = Event.objects.all()
    return render(request, 'catalog.html', {'events': events})

def event_view(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'events.html', {'event': event})

def add_to_cart(request, event_id):
    cart = request.session.get('cart', [])
    if event_id not in cart:
        cart.append(event_id)
        request.session['cart'] = cart
    return redirect('catalog.html')

def remove_from_cart(request, event_id):
    cart = request.session.get('cart', [])
    if event_id in cart:
        cart.remove(event_id)
        request.session['cart'] = cart
    return redirect('cart.html')

def cart_view(request):
    cart = request.session.get('cart', [])
    cart_events = Event.objects.filter(id__in=cart)
    return render(request, 'cart.html', {'events': cart_events})



