#!/usr/bin/env python3
from glob import glob
from os import walk
from os.path import (
    abspath,
    dirname,
    join as join_path)
from setuptools import setup
import versioneer


def enumerate_static_content(basedir_list):
    """Recursively enumerate static content to easily include data_files"""
    file_list = []
    for basedir in basedir_list:
        for path, _, files in walk(basedir):
            file_list.append((path, [join_path(path, filename) for filename in files if filename not in EXCLUDE_FILES]))
    return file_list


CURDIR = abspath(dirname(__file__))
EXCLUDE_FILES = (
    'constraints.txt',
    'interactive',
    'pip.ini',
    'pip.ini.socks',
    '.gitignore')
LICENSE = 'Proprietary'

PACKAGE_DATA_DIRS = []
SCRIPTS = glob('bin/*')

DATA_FILE_LIST = enumerate_static_content(PACKAGE_DATA_DIRS)

# If you use entry points, you can put them in setup.cfg
# ENTRY_POINTS = {
#     'console_scripts': [
#         'cli_app = app:main',
#     ],
# },

setup(
    cmdclass=versioneer.get_cmdclass(),
    version=versioneer.get_version(),
    data_files=DATA_FILE_LIST,
    scripts=SCRIPTS)
