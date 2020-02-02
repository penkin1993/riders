import sys
import pytest

import numpy as np

sys.path.append("..")

from get_schedule import GetSchedule


def test_get_time_generator():
    gets_shedule = GetSchedule(5, np.array([]), {})
    time_generator = gets_shedule._get_time_generator(6, 12)
    assert list(time_generator).__len__() == 6


# TODO: add hypotesis !!!!


