from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from .models import RestaurantLocation

def restaurant_listview(request):
    template_name = 'restaurants/restaurants_list.html'
    context = {
        "object_list": [1, 2, 3]
    }
    return render(request, template_name, context)

def home(request):
    return render(request, "base.html", {})
