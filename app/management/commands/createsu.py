import os

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username="admin").exists():
            DJANGO_SU_NAME = os.environ.get('DJANGO_SU_NAME')
            DJANGO_SU_EMAIL = os.environ.get('DJANGO_SU_EMAIL')
            DJANGO_SU_PASSWORD = os.environ.get('DJANGO_SU_PASSWORD')

            User.objects.create_superuser(DJANGO_SU_NAME, DJANGO_SU_EMAIL, DJANGO_SU_PASSWORD)
