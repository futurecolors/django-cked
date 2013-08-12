import os

from setuptools import setup, find_packages


# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='django-cked-fc',
    version='0.1',
    author='Future Colors (original by Svyatoslav Bulbakha)',
    author_email='info@futurecolors.ru',
    description='CKEditor and elFinder integration for Django Framework.',
    license='BSD',
    keywords='django, ckeditor, elfinder, wysiwyg, upload',
    url='https://github.com/futurecolors/django-cked',
    packages=find_packages(),
    long_description=read('README.rst'),
    install_requires=[
        'pytils'
    ],
)
