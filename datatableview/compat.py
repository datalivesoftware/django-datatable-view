# -*- encoding: utf-8 -*-
""" Backports of code left behind by new versions of Django. """

import django
from django.utils.html import escape
try:
    from django.utils.encoding import escape_uri_path as django_escape_uri_path
except ImportError:
    django_escape_uri_path = None


def escape_uri_path(path):
    if django_escape_uri_path:
        return django_escape_uri_path(path)
    return escape(path)
