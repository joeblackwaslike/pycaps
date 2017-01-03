"""
pycaps.caps
~~~~~~~~~~~~~~~~~~~~

This module holds the linux capabilities class.

:copyright: (c) 2016 by Joe Black.
:license: Apache2.
"""

import ctypes
import ctypes.util


def get_caps():
    """Returns an instance of LinuxCaps"""
    return LinuxCaps()


class LinuxCaps:
    """Represents the current capabilities of the current process."""
    _flag_map = dict(e='effective', i='inhertiable', p='permitted')

    def __init__(self, source='proc'):
        self.source = source
        self._init()
        if self.lib:
            self._set_from(source)

    def __repr__(self):
        cls_name = type(self)
        caps = ', '.join(self.caps)
        flags = ', '.join([name for name in self._flag_map.values()
                           if getattr(self, name)])
        return '%s(flags: %s, caps: %s)' % (cls_name, flags, caps)

    def __str__(self):
        return ', '.join(self.caps)

    def __contains__(self, key):
        return key.lower() in self.caps

    def __getitem__(self, key):
        return key.lower() in self

    def __getattr__(self, key):
        return self[key]

    def _parse_caps(self, caps):
        caps = caps.decode()
        caps = caps[2:]
        if '+' in caps:
            op = '+'
        elif '-' in caps:
            op = '-'
        caps, flags = caps.split(op)
        caps = caps.split(',')
        caps = tuple([cap.replace('cap_', '') for cap in caps])
        flags = tuple([self._flag_map[flag] for flag in flags])
        return caps, flags

    def _init(self):
        self.lib = ctypes.util.find_library('cap')
        if self.lib:
            self.libcap = ctypes.cdll.LoadLibrary(self.lib)
            self.libcap.cap_to_text.restype = ctypes.c_char_p
        self.clear()

    def clear(self):
        """Clears the current LinuxCaps object."""
        self.caps = ()
        self.flags = ()
        for name in self._flag_map.values():
            setattr(self, name, False)

    def _set_from(self, source):
        init_func_name = '_set_from_%s' % source
        init_func = getattr(self, init_func_name)
        init_func()

    def _set_from_proc(self):
        cap_t = self.libcap.cap_get_proc()
        caps = self.libcap.cap_to_text(cap_t, None)
        self.libcap.cap_free(cap_t)
        if caps:
            self.caps, self.flags = self._parse_caps(caps)
            for flag in self.flags:
                setattr(self, flag, True)
