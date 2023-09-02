from rest_framework import serializers
from api.models import Library


class LibrarySerializer(serializers.ModelSerializer):
    groupId = serializers.CharField(source='group_id')
    artifactId = serializers.CharField(source='artifact_id')
    version = serializers.CharField()
    hash = serializers.CharField()

    class Meta:
        model = Library
        fields = ('groupId', 'artifactId', 'version', 'hash')