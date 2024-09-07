from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from notify.models import Address


class AddressListView(ListView):
    model = Address


class AddressCreateView(CreateView):
    model = Address
    fields = ["name", "email"]
    success_url = reverse_lazy('notify:address-list')


class AddressUpdateView(UpdateView):
    model = Address
    fields = ["name", "email"]
    success_url = reverse_lazy('notify:address-list')


class AddressDeleteView(DeleteView):
    model = Address
    fields = ["name", "email"]
    success_url = reverse_lazy('notify:address-list')
