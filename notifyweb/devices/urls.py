from django.urls import path

from .views import DeviceListView, DeviceCreateView, DeviceUpdateView, DeviceDeleteView

app_name = 'devices'

urlpatterns = [
    path("", DeviceListView.as_view(), name="list"),
    path("add/", DeviceCreateView.as_view(), name="add"),
    path("<int:pk>/", DeviceUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", DeviceDeleteView.as_view(), name="delete"),
]
