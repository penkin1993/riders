import numpy as np


def test_rcs_get_combinations_and_set_combinations_simple(rcs):

    assert rcs.get_combinations(("d",), ("c",))[0].shape == (63, 17)
    assert rcs.get_combinations(("d", "c"), ("c",))[0].shape == (82, 17)
