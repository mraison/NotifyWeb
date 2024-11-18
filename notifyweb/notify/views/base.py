# Create your views here.
import os
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import logging
import requests

from django.views.generic.list import ListView
from ..serializers.device import DeviceSerializer
from ..models import Device

logger = logging.getLogger("dummy")

node_manager_url = os.environ.get('NODE_MANAGER_URL', 'http://127.0.0.1:8888/config')

def SystemConfig(request):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    payload = serializer_class(queryset, many=True).data
    template = loader.get_template("notify/index.html")
    context = {
        'config': payload
    }

    if request.method == 'GET':
        return HttpResponse(template.render(context, request))

    if request.method == 'POST':
        node_count = request.POST.get('node_count', 1)
        requests.post(
            node_manager_url,
            json={
                'node_count': int(node_count)
            }
        )

        return HttpResponse(template.render(context, request))


