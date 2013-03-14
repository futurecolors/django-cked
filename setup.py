import os

from setuptools import setup, find_packages


# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-cked',
    version='0.0.8',
    author='Svyatoslav Bulbakha',
    author_email='mail@ssbb.me',
    description=('CKEditor and elFinder integration for Django Framework.'),
    license='BSD',
    keywords='django, ckeditor, elfinder, wysiwyg, upload',
    url='https://bitbucket.org/ssbb/django-cked',
    packages=find_packages(),
    long_description=read('README.rst')
)
