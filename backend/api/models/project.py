from django.db import models

from api.models.file import File


class Project(models.Model):
    name = models.CharField(max_length=128)


class ProjectVersion(models.Model):
    class Channel(models.TextChoices):
        DEV = 'DEV', 'Dev'
        BETA = 'BETA', 'Beta'
        STABLE = 'STABLE', 'Stable'

    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    version = models.CharField(max_length=128)
    channel = models.CharField(max_length=128, choices=Channel.choices, default=Channel.STABLE)

    created_at = models.DateTimeField(auto_now=True)

class ProjectBuild(models.Model):
    project_version = models.ForeignKey(ProjectVersion, on_delete=models.CASCADE)

    build_number = models.IntegerField()
    file = models.ForeignKey(File, on_delete=models.CASCADE)