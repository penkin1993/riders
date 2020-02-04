import sys
import pytest

import numpy as np

sys.path.append("..")

from riders_combination_storage import RidersCombinationsStorage


def test_rcs_get_and_set_simple():
    rcs = RidersCombinationsStorage({"a": (2, 3), "b": (2, 15), "c": (0, 7), "d": (13, 16), "e": (14, 16)})

    array = rcs.get_combinations(("d",), ("c",))
    ind = [1, 3, 45]
    new_array = array[ind, :]
    rcs.set_combinations(("d",), ("c",), ind, new_array)

    assert array.shape == (63, 17)

    array_ = rcs.get_combinations(("d", "c"), ("c",))
    ind_ = [1, 3, 45]
    new_array_ = array_[ind_, :]
    rcs.set_combinations(("d", "c"), ("c",), ind_, new_array_)

    

