from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models import ProjectVersion, ProjectBuild
from api.serializers import ProjectVersionSerializer, InfoSerializer


class ProjectVersionViewset(viewsets.ViewSet):
    def list(self, request, project_name: str):
        # @TODO
        # Do it properly, maybe?

        dev_versions = ProjectVersionSerializer(
            instance=ProjectVersion.objects.filter(
                project__name=project_name,
                channel=ProjectVersion.Channel.DEV,
            ),
            many=True,
        )

        beta_versions = ProjectVersionSerializer(
            instance=ProjectVersion.objects.filter(
                project__name=project_name,
                channel=ProjectVersion.Channel.BETA,
            ),
            many=True,
        )

        stable_versions = ProjectVersionSerializer(
            instance=ProjectVersion.objects.filter(
                project__name=project_name,
                channel=ProjectVersion.Channel.STABLE,
            ),
            many=True,
        )

        return Response({
            'release_channel': {
                'dev': dev_versions.data,
                'beta': beta_versions.data,
                'stable': stable_versions.data,
            }
        })

class ProjectInfoViewset(viewsets.ModelViewSet):
    serializer_class = InfoSerializer

    def get_queryset(self):
        qs = ProjectBuild.objects.filter(
            project_version__project__name__iexact=self.kwargs['project_name'],
        )

        if self.kwargs.get('channel'):
            qs = qs.filter(project_version__channel__iexact=self.kwargs['channel'])
        elif self.kwargs.get('build_number'):
            qs = qs.filter(build_number=self.kwargs['build_number'])

        
        return qs.order_by('-build_number')

    @action(detail=False, url_path=r'(?P<channel>\w+)/(?P<project_name>\w+)')
    def info(self, request, channel: str, project_name: str):
        latest_build = self.get_queryset().first()
        if latest_build is None:
            return Response(status=404)

        s = self.get_serializer(instance=latest_build)

        return Response(s.data)

    @action(detail=False, url_path=r'build/(?P<build_number>\d+)/(?P<project_name>\w+)')
    def info_build(self, request, build_number: int, project_name: str):
        latest_build = self.get_queryset().first()
        if latest_build is None:
            return Response(status=404)

        s = self.get_serializer(instance=latest_build)

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