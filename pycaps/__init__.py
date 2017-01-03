"""
PyCaps
~~~~~~~~~~~~~

Linux capabilities for python.

Example:
    >>> import pycaps
    >>> caps = pycaps.get_caps()

    >>> if caps['setgid']: print('setgid enabled')
    setgid enabled

    >>> if caps['setgid'] is pycaps.ENABLED: print('setgid enabled')
    setgid enabled
"""

import logging
from logging import NullHandler

from . import caps
from .caps import LinuxCaps, get_caps

__title__ = 'pycaps'
__version__ = '0.2.0'
__build__ = 0x000200
__author__ = "Joe Black <joe@valuphone.com>"
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2016 Joe Black'


DISABLED = False
ENABLED = True

logging.getLogger(__name__).addHandler(NullHandler())
