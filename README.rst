Django CKEd
===========

**CKEditor and elFinder integration for Django Framework.**

Provides a ``RichTextField`` and ``CKEditorWidget`` with upload and
browse support.

.. image:: https://bitbucket.org/ssbb/django-cked/src/default/cked/ckeditor.jpg
.. image:: https://bitbucket.org/ssbb/django-cked/src/default/cked/elfinder.jpg

Installation
------------

1. Install or add django-cked to your PYTHONPATH.
   `pip install django-cked` or `-e hg+https://bitbucket.org/ssbb/django-cked`
   
2. Add ``cked`` to your ``INSTALLED_APPS`` setting.

3. Set ``ELFINDER_OPTIONS`` in your settings:

::
    ELFINDER_OPTIONS = {
    ## required options
        'root': os.path.join(PROJECT_ROOT, 'media', 'uploads'),
        'URL': '/media/uploads/',
    }
4. Add CKEd URL include to your project ``urls.py`` file:
   ``url(r'^cked/', include('cked.urls')),``

Settings
--------

-  **CKEDITOR\_OPTIONS**: CKEditor config. See
   `http://docs.ckeditor.com/#!/guide/dev\_configuration`_.
-  **ELFINDER\_OPTIONS**: elFinder config. See
   `https://github.com/Studio-42/elFinder/wiki/Client-configuration-options`_

Usage
-----

Model field
~~~~~~~~~~~

::

    from django.db import models
    from cked.fields import RichTextField


    class Entry(models.Model):
        text = RichTextField()

Widget
~~~~~~

::

    from django import forms
    from cked.widgets import CKEditorWidget

    class MyForm(forms.Form):
        text = forms.CharField(widget=CKEditorWidget)

**NOTE**: If you are using custom forms, dont’r forget to include form
media to your template: ``{{ form.media }}``.

.. _`http://docs.ckeditor.com/#!/guide/dev\_configuration`: http://docs.ckeditor.com/#!/guide/dev_configuration
.. _`https://github.com/Studio-42/elFinder/wiki/Client-configuration-options`: https://github.com/Studio-42/elFinder/wiki/Client-configuration-options
