from setuptools import find_packages, setup

setup(
    name='LLMToolkit',
    packages=find_packages(include=['LLMToolkit']),
    include_package_data=True,
    version='0.0.0',
    description='LLMToolkit library',
    author='Wiktoria Dębowska, Dawid Drożdżyński, Jakub Filipiak, Miłosz Kozlicki',
    install_requires=[],
    extras_require={
        'dev': ['pytest==8.3.3'],
    }
)
