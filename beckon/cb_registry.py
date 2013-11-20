# -*- coding: utf-8 -*-

from collections import defaultdict


class CallbackRegistry(object):

    _registrations = defaultdict(list)

    def register_cb(self, msg, fn):
        self._registrations[msg].append(fn)

    def cb(self, msg, params):
        for fn in self._registrations[msg]:
            fn(params)
