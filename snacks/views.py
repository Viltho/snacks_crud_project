from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Snack
from django.urls import reverse_lazy

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'
    
class AboutPageView(TemplateView):
    template_name = 'about.html'
    
class SnackListView(ListView):
    template_name="snacks.html"
    model=Snack
    context_object_name = "snacks"

class SnackDetailsView(DetailView):
    template_name="snack_details.html"
    model=Snack
    
class SnackCreateView(CreateView):
    template_name='snack_create.html'
    model=Snack
    fields= ['name', 'description', 'purchaser']
    success_url=reverse_lazy('snacks')

class SnackUpdateView(UpdateView):
    template_name='snack_update.html'
    model=Snack
    fields="__all__"
    success_url=reverse_lazy('snacks')

class SnackDeleteView(DeleteView):
    template_name='snack_delete.html'
    model=Snack
    success_url=reverse_lazy('snacks')