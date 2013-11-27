# -*- coding: utf-8 -*-

from beckon import CallbackRegistry
from mock import sentinel
from mock import Mock
from unittest import TestCase


class _CalledException(Exception):
    pass


class TestCallbackRegistry(TestCase):

    def setUp(self):
        CallbackRegistry._registrations.clear()

    def test_call(self):
        reg = CallbackRegistry()
        fn = Mock()

        reg.register_cb(sentinel.msg, fn)

        reg.cb(sentinel.msg, sentinel.param)

        fn.assert_called_once_with(sentinel.param)

    def test_shared_registrations(self):
        reg1 = CallbackRegistry()
        fn = Mock()

        reg1.register_cb(sentinel.msg, fn)

        del reg1

        reg2 = CallbackRegistry()
        reg2.cb(sentinel.msg, sentinel.param)

        fn.assert_called_once_with(sentinel.param)

    def test_accept(self):
        reg = CallbackRegistry()

        @reg.accept(sentinel.msg)
        def fn(params):
            raise _CalledException()

        self.assertRaises(_CalledException, reg.cb, sentinel.msg, sentinel.param)

    def test_emit(self):
        reg = CallbackRegistry()

        def cb(*args):
            if args[0] == sentinel.params:
                raise _CalledException()

        @reg.emit(sentinel.msg)
        def f(*args):
            return sentinel.params

        reg.register_cb(sentinel.msg, cb)

        self.assertRaises(_CalledException, f)
