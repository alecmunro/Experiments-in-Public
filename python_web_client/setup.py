import os
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'zope.interface>=3.8.0',#Required to avoid dependency mismatch
    'pyramid',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'requests',
    'mako',
    'sphinx',#docs
    'mock',#testing
    'selenium',#testing
    'nose'#testing
    ]

setup(name='pwc',
      version='0.1',
      description='Python Web Client',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Alec Munro',
      author_email='alecmunro@gmail.com',
      url='',
      keywords='web pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires = requires,
      tests_require = requires,
      test_suite="pwc",
      entry_points = """\
      [paste.app_factory]
      main = pwc:main
      """,
      paster_plugins=['pyramid'],
      )
