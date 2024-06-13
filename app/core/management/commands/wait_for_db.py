# wait_for_db 
# => Django가 DB가 준비될 때까지 연결을 재시도하게 해주시 위해 필요
# => 왜 이렇게 하나요? 하나의 도커 이미지에 각 컨테이너 (app, db)가 존재하기 때문에 

# Django가 DB 연결에 실패했을 시, 재시도 하도록 만드는 로직을 추가
from django.core.management.base import BaseCommand
from django.db import connections
import time

# Operation Error & Psycopg2 Operation Error
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2OPsycopgpError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Wating for DB connection ...')

        is_db_connected = None
        while not is_db_connected:
            try:
                is_db_connected = connections['default']
            except (OperationalError, Psycopg2OPsycopgpError):
                self.stdout.write("Retrying DB connection ...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Congratue! PostgreSQL Connection Success!!!"))