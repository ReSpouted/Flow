from django.urls import path, include
from rest_framework import routers

from api.viewsets import *

r = routers.DefaultRouter(trailing_slash=True)

r.register(
    r'minecraft',
    MinecraftViewset,
    basename='minecraft',
)

r.register(
    r'info',
    ProjectInfoViewset,
    basename='info',
)

r.register(
    r'libraries',
    LibraryViewset,
    basename='libraries',
)

urlpatterns = [
    path('', include(r.urls)),
    path(r'versions/<str:project_name>', ProjectVersionViewset.as_view({'get': 'list'})),
]