#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name='connexion-example-app',
    packages=find_packages(),
    version='0.1.0',
    description='Example of a Connexion application.',
    author='Zalando SE',
    url='https://github.com/hjacobs/connexion-example',
    license='MIT',
    install_requires=['connexion'],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    long_description='Example of a Connexion application.',
    entry_points={'console_scripts': ['connexion-example-app = app:main']},
)
