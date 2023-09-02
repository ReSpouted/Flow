from typing import Any, Optional
import requests

from django.core.management import BaseCommand
from django.core.management.base import CommandParser


class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('mc_version')

    def handle(self, *args: Any, **options: Any) -> str | None:
        versions_manifest = requests.get('https://piston-meta.mojang.com/mc/game/version_manifest_v2.json').json()

        for version in versions_manifest['versions']:
            if version == options['mc_version']:
                print('MC Version found')
                print('@TODO/ Add in DB + libraries, download the jar to get its MD5, remove it')
                break
