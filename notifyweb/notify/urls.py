from django.urls import path

from .views.base import index
from .views.address import AddressListView, AddressCreateView, AddressUpdateView, AddressDeleteView
from .views.device import DeviceListView, DeviceCreateView, DeviceUpdateView, DeviceDeleteView

app_name = 'notify'

urlpatterns = [
    path("", index, name="index"),

    path("address/", AddressListView.as_view(), name="address-list"),
    path("address/add/", AddressCreateView.as_view(), name="address-add"),
    path("address/<int:pk>/", AddressUpdateView.as_view(), name="address-update"),
    path("address/<int:pk>/delete/", AddressDeleteView.as_view(), name="address-delete"),

    path("device", DeviceListView.as_view(), name="device-list"),
    path("device/add/", DeviceCreateView.as_view(), name="device-add"),
    path("device/<int:pk>/", DeviceUpdateView.as_view(), name="device-update"),
    path("device/<int:pk>/delete/", DeviceDeleteView.as_view(), name="device-delete"),
]
