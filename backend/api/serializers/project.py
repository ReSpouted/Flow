from rest_framework import serializers

from api.models import ProjectVersion, ProjectBuild

class ProjectVersionSerializer(serializers.ModelSerializer):
    version = serializers.CharField()

    class Meta:
        model = ProjectVersion
        fields = ('version',)

class InfoSerializer(serializers.ModelSerializer):
    project = serializers.CharField(source='project_version.project.name')
    release_channel = serializers.SerializerMethodField()
    build = serializers.IntegerField(source='build_number')
    version = serializers.CharField(source='project_version.version')
    file_name = serializers.CharField(source='file.filename')
    file_type = serializers.CharField(source='file.type')
    hash = serializers.CharField(source='file.hash')

    def get_release_channel(self, obj: ProjectBuild):
        match (obj.project_version.channel):
            case ProjectVersion.Channel.STABLE:
                return 0
            case ProjectVersion.Channel.BETA:
                return 1
            case ProjectVersion.Channel.DEV:
                return 2
            case other:
                return 3 # CUSTOM


    class Meta:
        model = ProjectBuild
        fields = ('project', 'release_channel', 'build', 'version', 'file_name', 'file_type', 'hash')
