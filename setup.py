from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='coverletter',
      version='0.1',
      description='cover letter generator',
      url='http://github.com/victorlau1/coverletter',
      author='Victor Lau',
      author_email='lau.victor.w@gmail.com',
      license='MIT',
      packages=['coverletter'],
      install_requires=[
            'python-docx'
      ],
      tests_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)