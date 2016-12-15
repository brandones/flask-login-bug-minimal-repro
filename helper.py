# -*- coding: utf-8 -*-
#
# helper.py
#
# Copyright 2016 Socos LLC
#


def do_thing(account):
    print 'Actual do_thing called'
    account.email += '-modified'
    account.put()
