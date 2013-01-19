# Django CKEd

**CKEditor and elFinder integration for Django Framework.**

Provides a `RichTextField` and `CKEditorWidget` with upload and
browse support.

----------

![CKEditor](https://bitbucket.org/ssbb/django-cked/raw/default/img/ckeditor.jpg)
![elFinder](https://bitbucket.org/ssbb/django-cked/raw/default/img/elfinder.jpg)

## Installation

1. Install or add django-cked to your PYTHONPATH.
   `pip install django-cked`
   `pip install -e hg+https://bitbucket.org/ssbb/django-cked#egg=django-cked`

2. Add ``cked`` to your ``INSTALLED_APPS`` setting.

3. Set ``ELFINDER_OPTIONS`` in your settings:

:::python
    ELFINDER_OPTIONS = {
    ## required options
        'root': os.path.join(PROJECT_ROOT, 'media', 'uploads'),
        'URL': '/media/uploads/',
    }

4. Add CKEd URL include to your project ``urls.py`` file:

:::python
   url(r'^cked/', include('cked.urls')),

## Settings

- **CKEDITOR_OPTIONS**: CKEditor config.
  See [http://docs.ckeditor.com/#!/guide/dev_configuration](http://docs.ckeditor.com/#!/guide/dev_configuration)
-  **ELFINDER_OPTIONS**: elFinder config. See
   [https://github.com/Studio-42/elFinder/wiki/Client-configuration-options](https://github.com/Studio-42/elFinder/wiki/Client-configuration-options)


## Usage

### Model field

:::python
    from django.db import models
    from cked.fields import RichTextField


    class Entry(models.Model):
        text = RichTextField()

### Widget

:::python
    from django import forms
    from cked.widgets import CKEditorWidget

    class MyForm(forms.Form):
        text = forms.CharField(widget=CKEditorWidget)

**NOTE**: If you are using custom forms, dont’r forget to include form
media to your template: `{{ form.media }}`
