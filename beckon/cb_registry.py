# -*- coding: utf-8 -*-

from collections import defaultdict


class CallbackRegistry(object):
    """
    The CallbackRegistry is the dispatcher in the callback system.

    Registrations are shared between multiple instances of a given CallbackRegistry.
    There's no need to pass the instance around, just create a new one wherever needed.
    """

    _registrations = defaultdict(list)

    def accept(self, msg):
        def decorator(f):
            def inner(*args):
                return f(*args)
            self.register_cb(msg, inner)
            return inner
        return decorator

    def emit(self, msg):
        def decorator(f):
            def decorated(*args):
                result = f(*args)
                self.cb(msg, result)
                return result
            return decorated
        return decorator

    def register_cb(self, msg, fn):
        """
        Register a new callback function for a given message key
        """
        self._registrations[msg].append(fn)

    def cb(self, msg, params):
        """
        Launches the callback chain for a given message key
        """
        for fn in self._registrations[msg]:
            fn(params)
