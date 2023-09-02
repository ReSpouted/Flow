from rest_framework import serializers
from api.models import Minecraft


class MinecraftSerializer(serializers.ModelSerializer):
    minecraft_version = serializers.CharField(source='version')
    minecraft_hash = serializers.CharField(source='hash')
    # Temporary
    libraries = serializers.SerializerMethodField()

    def get_libraries(self, obj):
        return []

    class Meta:
        model = Minecraft
        fields = ('minecraft_version', 'minecraft_hash', 'libraries')