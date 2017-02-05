"""Test serialization and deserialization of quantities via pickle."""
from pickle import dumps, loads
from units import unit, named_unit
from units.compatibility import within_epsilon
from units.registry import REGISTRY

def test_unit_pickle():
    arbitrary = unit('arbitrary')
    pickled = dumps(arbitrary)
    unpickled = loads(pickled)
    assert id(arbitrary) == id(unpickled)
    assert arbitrary == unpickled

def test_leaf_pickle():
    arbitrary = unit('arbitrary')
    v = arbitrary(3.0)
    pickled = dumps(v)
    unpickled = loads(pickled)
    assert within_epsilon(v, unpickled)

def test_composed_pickle():
    arbitrary = unit('arbitrary')
    v = arbitrary(3.0) * arbitrary(3.0)
    pickled = dumps(v)
    unpickled = loads(pickled)
    assert within_epsilon(v, unpickled)

def test_named_pickle():
    named = named_unit('S', 'N', 'D')
    v = named(3.0)
    pickled = dumps(v)
    unpickled = loads(pickled)
    assert within_epsilon(v, unpickled)

def teardown_module(module):
    # Disable warning about not using module.
    # pylint: disable=W0613
    """Called after running all of the tests here."""
    REGISTRY.clear()
