from django.db import models

from api.models.minecraft import Minecraft
from api.models.project import ProjectBuild

class Library(models.Model):
    build = models.ForeignKey(ProjectBuild, on_delete=models.CASCADE, null=True, related_name='project_libraries')
    mc_version = models.ForeignKey(Minecraft, on_delete=models.CASCADE, null=True, related_name='mc_libraries')

    group_id = models.CharField(max_length=128)
    artifact_id = models.CharField(max_length=128)
    version = models.CharField(max_length=128)
    hash = models.CharField(max_length=32)