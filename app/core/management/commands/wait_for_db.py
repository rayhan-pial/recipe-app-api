"""
Django comand to wait for the database to be available
"""
import time

from psycopg2 import OperationalError as Psycopg20Error

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command for wait of DB"""

    def handle(self, *args, **options):
        """Entry point for command"""
        self.stdout.write('waiting for database........')
        db_up = False

        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg20Error, OperationalError):
                self.stdout.write('Database unavailable, wait for 1 sec....')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available'))
