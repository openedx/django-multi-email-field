|ci-badge| |coverage| |pypi|

Field and widget to store a list of e-mail addresses in a `Django <https://www.djangoproject.com>`_ project.

It provides:

* A form field and a form widget to edit a list of e-mails in a Django form;
* A model field to store the captured list of e-mails;

==================
COMPATIBILITY
==================

* Python 3.8
* Django 3.2 and 4.0

==================
INSTALL
==================

For now:

::

    pip install django-multi-email-field

==================
USAGE
==================

* Add ``multi_email_field`` to your ``INSTALLED_APPS``:

::

    # settings.py
    INSTALLED_APPS = (
    ...
    'multi_email_field',
    )

* Use the provided form field and widget:

::

    # forms.py
    from django import forms
    from multi_email_field.forms import MultiEmailField

    class SendMessageForm(forms.Form):
        emails = MultiEmailField()

==================
IN YOUR MODELS
==================

If you want to store a list of e-mails, you can use this:

::

    from django.db import models
    from multi_email_field.fields import MultiEmailField

    class ContactModel(models.Model):
        emails = MultiEmailField()

==================
AUTHORS
==================

    * Created by `Florent Lebreton <https://github.com/fle/>`_
    * Maintained by Openedx


.. |coverage| image:: https://img.shields.io/codecov/c/github/openedx/django_multi_email_field
    :target: https://codecov.io/gh/openedx/django-multi-email-field?branch=master
.. |pypi| image:: https://img.shields.io/pypi/v/dj_multi_email_field.svg
    :target: https://pypi.python.org/pypi/dj_multi_email_field/
.. |ci-badge| image:: https://github.com/openedx/django-multi-email-field/workflows/Python%20CI/badge.svg?branch=master
    :target: https://github.com/openedx/django-multi-email-field/actions?query=workflow%3A%22Python+CI%22
    :alt: CI