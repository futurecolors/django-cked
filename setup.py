import os

from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='django-cked-fc',
    version='0.1.1',
    author='Future Colors (original by Svyatoslav Bulbakha)',
    author_email='info@futurecolors.ru',
    description='CKEditor and elFinder integration for Django Framework.',
    license='BSD',
    keywords='django, ckeditor, elfinder, wysiwyg, upload',
    url='https://github.com/futurecolors/django-cked',
    packages=['cked'],
    long_description=README,
    include_package_data=True,
    install_requires=[
        'pytils'
    ],
)
