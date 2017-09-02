from setuptools import setup, find_packages

import os
description = 'Dummy App'

setup(
    name='dummyapp',
    version='0.1',
    scripts=['dummy.py'],
    zip_safe=False,
    description=description,
    url='http://github.com/karmab/dummy',
    author='Karim Boumedhel',
    author_email='karimboumedhel@gmail.com',
    license='ASL',
    install_requires=[
        'flask',
    ],
)
