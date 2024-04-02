from django.shortcuts import render
from .models import Smoothie

# Create your views here.

def all_smoothies(request):
    """ A view to show all products, including sorting and search queries """

    smoothies = Smoothie.objects.all()

    context = {
        'smoothies': smoothies,
    }

    return render(request, 'smoothies/smoothies.html', context)