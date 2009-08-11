"""Provides support for quantities and units, which strictly disallow
invalid operations between incompatible quantities. For example, we cannot add 
2 metres to 5 seconds, because this doesn't make sense.

@requires: U{Python<http://python.org/>} >= 2.5
@since: 2009-Aug-10
@status: under development
"""

__author__    = 'Aran Donohue'
__version__   = '0.00'
__copyright__ = '2009'
__license__   = 'Python Software Foundation License'
__contact__   = 'aran@arandonohue.com'

REGISTRY = {}

import units.si

import units.leaf_unit
import units.named_composed_unit


def unit(unit_str, registry=REGISTRY):
    """Create a unit object from a given string specification"""
    if unit_str in registry:
        return registry[unit_str]
    if units.si.can_make(unit_str, registry):
        return units.si.make(unit_str, registry)
    else:
        return units.leaf_unit.make(unit_str, is_si=False, registry=registry)