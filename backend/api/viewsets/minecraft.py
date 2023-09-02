from rest_framework import viewsets
from rest_framework.request import Request

from api.models import Minecraft
from api.serializers import MinecraftSerializer


class MinecraftViewset(viewsets.ModelViewSet):
    queryset = Minecraft.objects.all()
    serializer_class = MinecraftSerializer