# -*- coding: utf-8 -*-

from beckon import CallbackRegistry
from mock import sentinel
from mock import Mock
from unittest import TestCase


class TestCallbackRegistry(TestCase):

    def test_call(self):
        reg = CallbackRegistry()
        fn = Mock()

        reg.register_cb(sentinel.msg, fn)

        reg.cb(sentinel.msg, sentinel.param)

        fn.assert_called_once_with(sentinel.param)
