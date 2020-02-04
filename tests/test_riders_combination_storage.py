import numpy as np


def test_rcs_get_combinations_and_set_combinations_simple(rcs):

    assert rcs.get_combinations(("d",), ("c",)).shape == (63, 17)
    assert rcs.get_combinations(("d", "c"), ("c",)).shape == (84, 17)


def test_rcs_get_best_combination_and_set_best_combination_simple(rcs):  # TODO: Добавить фикстуру

    rcs.best_combination = ("c",), np.array([0, 1, 4]), np.array([100, 10, 20])
    assert rcs.best_combination == (('c',), ((0, 3),), 1)

    rcs.best_combination = ("d", "c",), np.array([12, 3, 4]), np.array([10, 10, 10])
    assert rcs.best_combination == (('c',), ((0, 3),), 1)

    rcs.best_combination = ("c", "q",), np.array([31, 0, 12]), np.array([20, 20, 20])
    assert rcs.best_combination == (('c',), ((0, 3),), 1)

    rcs.best_combination = ("c",), np.array([0, 1, 4]), np.array([100, 10, 20])
    assert rcs.best_combination == (('c',), ((0, 3),), 1)

    rcs.best_combination = ("d", "c", "c"), np.array([1, 2]), np.array([1, 5])
    assert rcs.best_combination == (('d', 'c', 'c'), ((14, 16), (0, 5), (0, 5)), 1)
