from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from devices.models import Device


def index(request):
    return HttpResponse("Hello, world. You're at the devices index.")


class DeviceListView(ListView):
    model = Device


class DeviceCreateView(CreateView):
    model = Device
    fields = ["name", "subscribers"]
    success_url = reverse_lazy('devices:list')


class DeviceUpdateView(UpdateView):
    model = Device
    fields = ["name", "subscribers"]
    success_url = reverse_lazy('devices:list')


class DeviceDeleteView(DeleteView):
    model = Device
    fields = ["name"]
    success_url = reverse_lazy('devices:list')
