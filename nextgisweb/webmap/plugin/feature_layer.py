# -*- coding: utf-8 -*-
from .base import WebmapPlugin

from ...feature_layer import IFeatureLayer


@WebmapPlugin.registry.register
class FeatureLayerPlugin(WebmapPlugin):

    @classmethod
    def is_layer_supported(cls, layer, webmap):
        if IFeatureLayer.providedBy(layer):
            return ("webmap/plugin/FeatureLayer", True)