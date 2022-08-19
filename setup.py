#!/usr/bin/env python

from setuptools import setup, Require

setup(name='Positivity to Art - Models',
      version='0.0.4',
      description='Model Objects for Positivity to Art',
      author='Geryl Pelayo',
      author_email='hi@gerylpelayo.com',
      packages=['positivity_models'],
      install_requires=["sqlalchemy>=1.4.39",
                        "SQLAlchemy-serializer>=1.4.1"])
