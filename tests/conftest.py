import sys
import pytest

import numpy as np

sys.path.append("..")

from riders_combination_storage import RidersCombinationsStorage


@pytest.fixture(scope="module")
def rcs(request):
    rcs_object = RidersCombinationsStorage({"a": (2, 3), "b": (2, 15), "c": (0, 7), "d": (13, 16), "e": (14, 16)})

    array = rcs_object.get_combinations(("d",), ("c",))
    ind = [1, 3, 45, 5]
    new_array = array[ind, :]
    rcs_object.set_combinations(("d",), ("c",), ind, new_array)

    array_ = rcs_object.get_combinations(("d", "c"), ("c",))
    ind_ = [1, 45]
    new_array_ = array_[ind_, :]
    rcs_object.set_combinations(("d", "c"), ("c",), ind_, new_array_)

    yield rcs_object

    del rcs_object


