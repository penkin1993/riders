import sys
import pytest

import numpy as np

sys.path.append("..")

from riders_combination_storage import RidersCombinationsStorage
from riders_iterator import RidersCombinationsChecker


@pytest.fixture(scope="module")
def rcs():
    rcs_object = RidersCombinationsStorage({"a": (2, 3), "b": (2, 15), "c": (0, 7), "d": (13, 16), "e": (14, 16)})

    array, not_duplicate_index = rcs_object.get_combinations(("d",), ("c",))
    ind = np.array([1, 3, 45, 5])

    new_array = array[ind, :]
    rcs_object.set_combinations(("d", "c"), not_duplicate_index, ind, new_array)

    array_, not_duplicate_index_ = rcs_object.get_combinations(("d", "c"), ("c",))
    ind_ = np.array([1, 45])

    new_array_ = array_[ind_, :]
    rcs_object.set_combinations(("d", "c", "c",), not_duplicate_index_, ind_, new_array_)

    yield rcs_object

    del rcs_object


@pytest.fixture(scope="module")
def rc():
    rider_requirements = np.array([2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0])
    comb_check = RidersCombinationsChecker(rider_requirements)

    yield comb_check

    del comb_check


