from django.urls import path

from .views import AddressListView, AddressCreateView, AddressUpdateView, AddressDeleteView

app_name = 'addresses'

urlpatterns = [
    path("", AddressListView.as_view(), name="list"),
    path("add/", AddressCreateView.as_view(), name="add"),
    path("<int:pk>/", AddressUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", AddressDeleteView.as_view(), name="delete"),
]
