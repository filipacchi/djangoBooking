from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Booking

def bookings(request):
    mybookings = Booking.objects.all().values()
    template = loader.get_template('all_bookings.html')
    context = {
        'mybookings': mybookings,
    }
    return HttpResponse(template.render(context, request))