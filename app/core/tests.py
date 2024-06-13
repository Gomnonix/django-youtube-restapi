"""
Test custom Django management commands.
"""
from unittest.mock import patch

from psycopg2 import OperationalError as Psycopg2OPsycopgpError

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch('django.db.utils.ConnectionHandler.__getitem__') # 이 함수를 가로챈다.
class CommandTests(SimpleTestCase): #테스트를 위해서 테스트케이스 필요
    """Test commands."""

    # wait_for_db 명령어가 DB가 준비되었을 때 잘 동작하는 지 체크하는 함수
    def test_wait_for_db_ready(self, patched_getitem): 
        """Test waiting for database if database ready."""
        patched_getitem.return_value = True

        call_command('wait_for_db')

        self.assertEqual(patched_getitem.call_count, 1)
 
    # db연결에 오류가 발생했다고 가정을 하고 테스트
    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_getitem):
        """Test waiting for database when getting OperationalError."""
        patched_getitem.side_effect = [Psycopg2OPsycopgpError] + \
            [OperationalError] * 5 + [True]

        call_command('wait_for_db')

        self.assertEqual(patched_getitem.call_count, 7)

    # docker-compose run --rm app sh -c 'python manage.py test core'
