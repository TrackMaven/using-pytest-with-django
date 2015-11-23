#!/usr/bin/env python
import os
import sys
from django.core.management.base import CommandError


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

    from django.core.management import execute_from_command_line
    if sys.argv[1] == 'test':
        raise CommandError('To run the test suite, invoke `py.test`. `manage.py test` is not used to run tests.')
    execute_from_command_line(sys.argv)
