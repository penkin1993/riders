import itertools
import time

from typing import Dict, Tuple, Iterable, Hashable

import numpy as np


class RidersCombinationsStorage:
    """
    Класс для хранения всей информации о комбинациях времени работы курьеров
    """
    def __init__(self,
                 id_rider2time: Dict[Hashable, Tuple[int, int]],
                 working_duration: int = 17,
                 working_time_constraint: int = 3):
        """
        :param working_time_constraint: minimum number of hour for a courier
        :param id_rider2time: information with courier id and pair (start_hour, end_hour)
        """
        self.__ids = None
        self._np_rider2time_borders, self._rider2time_borders = self.__rider_combinations_init(id_rider2time,
                                                                                               working_duration,
                                                                                               working_time_constraint)
        # Храним границы в self._rider2time_borders:
        # [((id1_border), (id2_border), (id3_border), (id4_border)), (...), (....)].
        self.__best_combination = ((), -1, np.inf)
        # (new_id, row_indexes, loss)

    @property
    def best_combination(self):
        return (self.__best_combination[0],
                self._rider2time_borders[self.__best_combination[0]][self.__best_combination[1][0]],
                self.__best_combination[2])

    @best_combination.setter
    def best_combination(self, value: Tuple[Tuple, np.ndarray, np.ndarray]):
        min_loss = min(value[2])
        if self.__best_combination[2] > min_loss:
            self.__best_combination = value[0], [np.argmin(value[2])], min_loss

    @property
    def ids(self):
        return self.__ids

    @ids.setter
    def ids(self, value):
        raise Exception("You can not change this field")

    @staticmethod
    def __get_time_variants(start_hour: int, end_hour: int,
                            working_time_constraint: int, working_duration: int) -> Iterable:
        """
        :param start_hour: start hour of rider (possible)
        :param end_hour: end hour of rider (possible)
        :return:
        """
        assert end_hour < working_duration
        possible_intervals = itertools.combinations(np.arange(start_hour, end_hour + 1), 2)
        constraints_intervals = itertools.filterfalse(lambda x: x[1] - x[0] < working_time_constraint - 1,
                                                      possible_intervals)
        return constraints_intervals  # и сразу записать в массив

    def __add_rider(self, start_hour: int, end_hour: int, working_duration: int, working_time_constraint) -> Tuple:
        """
        :param start_hour:
        :param end_hour:
        :param working_duration:
        :param working_time_constraint:
        :return:
        """
        constraints_intervals = self.__get_time_variants(start_hour, end_hour,
                                                         working_time_constraint, working_duration)
        np_constraints_intervals_ = []
        constraints_intervals_ = []
        for interval in constraints_intervals:
            working_hours = np.zeros(working_duration)
            working_hours[slice(interval[0], interval[1] + 1)] += 1
            np_constraints_intervals_.append(working_hours)

            constraints_intervals_.append((interval, ),)

        if len(np_constraints_intervals_):
            np_constraints_intervals_ = np.vstack(np_constraints_intervals_)
        else:
            np_constraints_intervals_ = np.array(np_constraints_intervals_)

        return np_constraints_intervals_, constraints_intervals_

    def __rider_combinations_init(self, id_rider2time: Dict, working_duration: int, working_time_constraint: int):
        """
        Инициализаиця первичных массивов
        :param id_rider2time:
        :param working_duration:
        :param working_time_constraint:
        :return:
        """
        np_rider2time_borders = {}
        rider2time_borders = {}

        for id_rider in id_rider2time:
            np_constraints_intervals, constraints_intervals = (self.__add_rider(*id_rider2time[id_rider],
                                                                                working_duration,
                                                                                working_time_constraint))
            # проверка что данный курьер при ограничения на время сможет работать
            if np_constraints_intervals.shape[0] != 0:
                np_rider2time_borders[(id_rider,)], rider2time_borders[(id_rider,)] = (
                    np_constraints_intervals, np.array(constraints_intervals))

        self.__ids = list(rider2time_borders.keys())

        return np_rider2time_borders, rider2time_borders

    def get_combinations(self, id1: Tuple, id2: Tuple) -> Tuple[np.ndarray, np.array]:
        """
        Составления комбинаций для доступа по ключу
        :param id1:
        :param id2:
        :return:
        """
        assert len(id1) | len(id2)

        if len(id1) == 0:
            return self._np_rider2time_borders[id2], np.array([])

        if len(id2) == 0:
            return self._np_rider2time_borders[id1], np.array([])

        intervals1 = self._np_rider2time_borders[id1]
        intervals2 = self._np_rider2time_borders[id2]

        # ts = time.time()
        # print(ts)

        intervals_matrix = (intervals1[:, None, :] + intervals2).reshape(-1, intervals1.shape[1])

        # # удаление дубликатов
        intervals_matrix, not_duplicate_index = np.unique(intervals_matrix, axis=0, return_index=True)
        return intervals_matrix, not_duplicate_index

    def set_combinations(self, new_id: Tuple, not_duplicate_index: np.ndarray,
                         row_indexes: np.ndarray, intervals_matrix: np.ndarray):
        """
        :param new_id:
        :param not_duplicate_index:
        :param row_indexes:
        :param intervals_matrix:
        :return:
        """
        if new_id in self._np_rider2time_borders:
            return

        self._np_rider2time_borders[new_id] = intervals_matrix
        self._rider2time_borders[new_id] = []

        new_combinations = np.array(list(itertools.product(self._rider2time_borders[new_id[:-1]],
                                                           self._rider2time_borders[new_id[-1:]])))

        new_combinations = new_combinations[not_duplicate_index]

        [self._rider2time_borders[new_id].append((*new_combinations[ind][0],
                                                  *new_combinations[ind][1])) for ind in row_indexes]

