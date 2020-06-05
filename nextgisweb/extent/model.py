# -*- coding: utf-8 -*-
from __future__ import division, absolute_import, print_function, unicode_literals

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declared_attr


class ExtentMixin(object):

    @declared_attr
    def extent_left(cls):
        return sa.Column(sa.Float, default=-180)

    @declared_attr
    def extent_right(cls):
        return sa.Column(sa.Float, default=+180)

    @declared_attr
    def extent_bottom(cls):
        return sa.Column(sa.Float, default=-90)

    @declared_attr
    def extent_top(cls):
        return sa.Column(sa.Float, default=+90)
