from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from .models import RestaurantLocation

def restaurant_listview(request):
    template_name = 'restaurants/restaurants_list.html'
    context = {
        "object_list": [1, 2, 3]
    }
    return render(request, template_name, context)

def home(request):
    return render(request, "base.html", {})

class RestaurantListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)

class RestaurantDetailView(LoginRequiredMixin, DetailView):
     def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)
