# -*- coding: utf-8 -*-
from __future__ import division, absolute_import, print_function, unicode_literals

from ..extent import ExtentMixin


class MapMixin(ExtentMixin):

    @classmethod
    def display_path(cls):
        raise NotImplementedError()
