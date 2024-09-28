import os
from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand
import sys

class PyTest(TestCommand):
    user_options = []

    def initialize_options(self):
        TestCommand.initialize_options(self)

    def finalize_options(self):
        TestCommand.finalize_options(self)

    def run_tests(self):
        # Import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main([])
        sys.exit(errno)

setup(
    name='NLPToolkit',
    packages=find_packages(include=['NLPToolkit']),
    version='0.0.0',
    description='NLPToolkit library',
    author='Wiktoria Dębowska, Dawid Drożdżyński, Jakub Filipiak, Miłosz Kozlicki',
    install_requires=[],  # Zależności Twojego projektu
    extras_require={
        'dev': ['pytest==8.3.3'],  # Zależności deweloperskie, w tym pytest
    },
    cmdclass={'test': PyTest},  # Ustawienie niestandardowej klasy dla testów
)
