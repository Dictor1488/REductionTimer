# -*- coding: utf-8 -*-
from .config_param_types import (
    CheckboxParameter,
    DropdownParameter,
    OptionItem
)
from .translations import Translator


class ReductionStyle(object):
    NEW = 'new'
    OLD = 'old'


class ConfigParams(object):

    def __init__(self):
        self._items_cache = None

        self.enabled = CheckboxParameter(
            ['enabled'],
            defaultValue=True
        )

        # --- Reduction Indicator (aiming timer) ---
        self.reductionEnabled = CheckboxParameter(
            ['reduction-enabled'],
            defaultValue=True
        )

        self.reductionStyle = DropdownParameter(
            ['reduction-style'],
            [
                OptionItem(ReductionStyle.NEW, 0, Translator.REDUCTION_STYLE_NEW),
                OptionItem(ReductionStyle.OLD, 1, Translator.REDUCTION_STYLE_OLD)
            ],
            defaultValue=ReductionStyle.NEW
        )

    def items(self):
        if self._items_cache is not None:
            return self._items_cache

        result = {}
        for attrName in dir(self):
            if attrName.startswith('_') or attrName == 'items':
                continue
            try:
                attr = getattr(self, attrName)
                if hasattr(attr, 'tokenName') and hasattr(attr, 'defaultValue'):
                    result[attr.tokenName] = attr
            except Exception:
                continue

        self._items_cache = result
        return self._items_cache


g_configParams = ConfigParams()
