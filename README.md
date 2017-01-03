# PyCaps

Linux capabilities for python.

Example:
    >>> import pycaps
    >>> caps = pycaps.get_caps()
    
    >>> if caps['setgid']: print('setgid enabled')
    >>> if caps['setgid'] is pycaps.ENABLED: print('setgid enabled')

Requirements:
* Linux
* libcap2
