import re
from setuptools import setup
# import ctypes.util

with open('pycaps/__init__.py', 'rt') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

with open('README.md', 'rt') as fd:
    readme = fd.read()

# if not ctypes.util.find_library('cap'):
#     raise RuntimeError('required lib: libcap2 not installed.')

setup(
    name='pycaps',
    version=version,
    description='Linux capabilities for python.',
    long_description=readme,
    keywords=['linux', 'capabilities', 'libcap2'],
    author='Joe Black',
    author_email='joeblack949@gmail.com',
    url='https://github.com/joeblackwaslike/pycaps',
    download_url='https://github.com/joeblackwaslike/pycaps/tarball/0.2.0',
    license='Apache 2.0',
    zip_safe=False,
    packages=['pycaps'],
    package_data={'': ['LICENSE']},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: POSIX :: Linux',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: System :: Systems Administration',
    ]
)
