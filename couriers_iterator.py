import itertools
import numpy as np

from typing import Dict, Tuple, Iterable


class CourierCombinationsStorage:
    #  Этот класс скорее самой структуры, которая хранить комбинацц и результаты
    """
    TODO: Docstring
    """
    def __init__(self,
                 id_rider2time: Dict[int, Tuple[int, int]],
                 working_duration: int = 17,
                 working_time_constraint: int = 3):
        """
        :param working_time_constraint: minimum number of hour for a courier
        :param id_rider2time: information with courier id and pair (start_hour, end_hour)
        """
        self._np_rider2time_borders, self._rider2time_borders = self.__rider_combinations_init(id_rider2time,
                                                                                               working_duration,
                                                                                               working_time_constraint)

    @staticmethod
    def __get_time_variants(start_hour: int, end_hour: int, working_time_constraint) -> Iterable:
        """
        :param start_hour: start hour of rider (possible)
        :param end_hour: end hour of rider (possible)
        :return:
        """
        possible_intervals = itertools.combinations(np.arange(start_hour, end_hour + 1), 2)
        constraints_intervals = itertools.filterfalse(lambda x: x[1] - x[0] < working_time_constraint,
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
        constraints_intervals = self.__get_time_variants(start_hour, end_hour, working_time_constraint)

        np_constraints_intervals = []
        for interval in constraints_intervals:
            working_hours = np.zeros(working_duration)
            working_hours[slice(*interval)] += 1

            np_constraints_intervals.append(working_hours)

        return np_constraints_intervals, list(constraints_intervals)

    def __rider_combinations_init(self, id_rider2time: Dict, working_duration: int, working_time_constraint: int):
        """
        :param id_rider2time:
        :param working_duration:
        :param working_time_constraint:
        :return:
        """
        np_rider2time_borders = {}
        rider2time_borders = {}

        for id_rider in id_rider2time:
            np_rider2time_borders, rider2time_borders = self.__add_rider(*id_rider2time[id_rider],
                                                                         working_duration,
                                                                         working_time_constraint)

        return np_rider2time_borders, rider2time_borders


    # !!! TODO Ключи == кортежи !!!!!




    # TODO Добавить методы записи и получения по ключу !!! (Реализовать комбинации !!!)

    # TODO: Возможно перенести часть бизнес логики составления комбинаций в этот класс

    # TODO: Добавить тесты !!!!

