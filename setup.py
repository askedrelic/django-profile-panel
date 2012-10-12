# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import profile_panel

setup(
    name             = 'django-profile-panel',
    version          = profile_panel.__version__,
    description      = '',
    long_description = '',

    author           = profile_panel.__author__,
    author_email     = 'askedrelic@gmail.com',
    url              = '',
    license          = open("LICENSE.txt").read(),

    packages         = ['profile_panel'],

    requires         = ['django', 'debug_toolbar'],
    zip_safe         = False,
)
