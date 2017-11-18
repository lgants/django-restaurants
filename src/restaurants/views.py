from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from .forms import RestaurantCreateForm, RestaurantLocationCreateForm
from .models import RestaurantLocation

class RestaurantListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)

class RestaurantDetailView(LoginRequiredMixin, DetailView):
     def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)

class RestaurantCreateView(LoginRequiredMixin, CreateView):
    form_class = RestaurantLocationCreateForm
    login_url = '/login/'
    template_name = 'form.html'
    #success_url = "/restaurants/"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(RestaurantCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Restaurant'
        return context
