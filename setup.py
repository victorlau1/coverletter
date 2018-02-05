from setuptools import setup
import unittest

def readme():
    with open('README.rst') as f:
        return f.read()

def my_test_suite():
      test_loader = unittest.TestLoader()
      test_suite = test_loader.discover('tests', pattern='test_*.py')
      return test_suite

setup(name='coverletter',
      version='0.1',
      description='cover letter generator',
      url='http://github.com/victorlau1/coverletter',
      author='Victor Lau',
      author_email='lau.victor.w@gmail.com',
      license='MIT',
      packages=['coverletter'],
      install_requires=[
            'python-docx',
            'textblob'
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
