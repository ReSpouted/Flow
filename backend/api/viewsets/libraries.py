from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models import Library, ProjectBuild
from api.serializers import LibrarySerializer


class LibraryViewset(viewsets.ModelViewSet):
    serializer_class = LibrarySerializer

    def get_queryset(self):
        return ProjectBuild.objects.filter(build_number=self.kwargs['build_number'])

    @action(detail=False, url_path=r'build/(?P<build_number>\w+)')
    def list_libraries(self, request, build_number: int):
        build = self.get_queryset().first()
        if build is None:
            return Response(status=404)

        s = self.get_serializer(instance=[x for x in build.project_libraries.all()], many=True)

        return Response(s.data)

    def list(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def create(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def retrieve(self, request, pk=None):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, pk=None):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, pk=None):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, pk=None):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)