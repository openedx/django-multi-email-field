import os
import re

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

def get_version(*file_paths):
    """
    Extract the version string from the file at the given relative path fragments.
    """
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    with open(filename, encoding='utf-8') as opened_file:
        version_file = opened_file.read()
        version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                                  version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


VERSION = get_version("multi_email_field", "__init__.py")


setup(
    name='django-multi-email-field',
    version=VERSION,
    author='Florent Lebreton',
    author_email='florent.lebreton@makina-corpus.com',
    url='https://github.com/openedx/django-multi-email-field',
    description="Provides a model field and a form field to manage list of e-mails",
    long_description=open(os.path.join(here, 'README.rst')).read() + '\n\n' +
        open(os.path.join(here, 'CHANGES')).read(),
    license='LGPL, see LICENSE file.',
    install_requires=['Django'],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Topic :: Utilities',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
    ],
)
