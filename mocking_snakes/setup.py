'''
Created on 2011-08-04

@author: Alec
'''

from distutils.core import setup
import setuptools

setup(name='mocking_snakes',
      version='0.1',
      description='Mock object libraries comparison',
      author='Alec Munro',
      author_email='alecmunro@gmail.com',
      url='http://http://alecmunro.blogspot.com/',
      package_dir = {'': 'src'},
      packages=['mocking_snakes'],
      install_requires=["mocker", "flexmock", "fudge"]
     )