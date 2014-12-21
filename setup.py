from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='cliresms',
    version='0.2.0',
    description='Send webtexts from the command line for Irish carriers',
    long_description=long_description,
    url='https://github.com/russelldavies/cliresms',
    author='Russell Davies',
    author_email='russell@zeroflux.net',
    license='Apache v2',
    keywords='console cli sms webtext',
    py_modules=['cliresms'],
    install_requires=[],
    extras_require = {
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    entry_points={
        'console_scripts': [
            'cliresms=cliresms:main',
        ],
    },
)
