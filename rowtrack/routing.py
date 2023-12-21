from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/<str:machine_slug>/', consumers.MachineConsumer.as_asgi()),
]