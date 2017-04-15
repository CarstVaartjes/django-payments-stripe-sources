#!/usr/bin/env python
from setuptools import setup


PACKAGES = [
    'payments_stripe_sources'
]

REQUIREMENTS = [
    'Django>=1.5',
    'django-payments>=0.6.4',
]

setup(
    name='django-payments-stripe-sources',
    author='Carst Vaartjes',
    author_email='carstvaartjes@gmail.com',
    description='A django-payments backend for the the Stripe Sources payment gateway',
    version='0.1',
    url='https://github.com/carstvaartjes/django-payments-stripe-sources',
    packages=PACKAGES,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Framework :: Django',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    install_requires=REQUIREMENTS,
    zip_safe=False)