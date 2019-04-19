from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
  long_description = f.read()

setup(
    name="openidcpy",
    version='0.8',
    description='A package that implements the Relying Party Authorization Code Flow for OpenId Connect',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='Apache 2.0',
    author='Usman Shahid',
    author_email='usman.shahid@intechww.com',
    url='https://github.com/intech-iiot/openidcpy',
    packages=['openidcpy'],
    tests_require=['mock==2.0.0'],
    install_requires=[
      'requests==2.20.0',
      'python-jose==3.0.1'
    ]
)
