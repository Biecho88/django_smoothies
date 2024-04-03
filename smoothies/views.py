from django.shortcuts import render, get_object_or_404
from .models import Smoothie

# Create your views here.

def all_smoothies(request):
    """ A view to show all products, including sorting and search queries """

    smoothies = Smoothie.objects.all()

    context = {
        'smoothies': smoothies,
    }

    return render(request, 'smoothies/smoothies.html', context)


def smoothie_detail(request, name ):
    """ A view to show individual product details """

    smoothie = get_object_or_404(Smoothie, pk = name)

    context = {
        'smoothie': smoothie,
    }

    return render(request, 'smoothies/smoothie_detail.html', context)