# -*- coding: utf-8 -*-
#
# test.py
#
# Copyright 2016 Socos LLC
#

import mock
import main
from flask_testing import TestCase


class TestCheck(TestCase):

    def create_app(self):
        # Flask apps testing. See: http://flask.pocoo.org/docs/testing/
        main.app.config['TESTING'] = True
        main.app.config['WTF_CSRF_ENABLED'] = False
        return main.app

    def setUp(self):
        self.client = main.app.test_client()

    @mock.patch('main.helper.do_thing')
    def test_check(self, do_thing_mock):
        self.client.get('/login')
        self.client.get('/check')
        self.assertEqual(do_thing_mock.call_count, 1)
        do_thing_mock.assert_called_with(main.user)

