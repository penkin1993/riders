import numpy as np
import time

from typing import Tuple, Iterable


class RidersCombinationsChecker:
    """
    Класс для проверки комбинаций на требования курьеров по зонам
    """
    def __init__(self, riders_in_zones: np.ndarray):
        """
        :param riders_in_zones:
        """
        self.__riders_in_zones = riders_in_zones

    def __call__(self, intervals_matrix: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        :param intervals_matrix:
        :return:
        """
        # assert intervals_matrix.shape[1] == self.__riders_in_zones.shape[0]
        # ts1 = time.time()

        diff = self.__riders_in_zones - intervals_matrix
        # ts2 = time.time()

        min_diff = np.min(diff, axis=1)
        # ts3 = time.time()

        row_indexes = np.where(min_diff > 0)[0]
        # ts4 = time.time()

        checked_intervals_matrix = intervals_matrix[row_indexes, :]
        # ts5 = time.time()

        loss = -np.sum(checked_intervals_matrix, axis=1)
        # ts6 = time.time()

        return row_indexes, checked_intervals_matrix, loss  # индексы, проверенная матрца, лосс в каждом случае


# TODO: Добавить тесты
