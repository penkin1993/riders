import itertools

import pandas as pd
import numpy as np

from typing import Union, Dict, Tuple, Iterable

# self.__stat_working_hour = stat_working_hour  # начало рабочего дня
# self.__end_working_hour = end_working_hour  # конец рабочего дня




class GetSchedule:
    """
    TODO: Docstring
    """
    def __init__(self, time_constraint: int, zone_load: np.ndarray, id_rider2time: Dict[int, Tuple[int, int]]):
        """
        :param time_constraint: minimum number of hour for a courier
        :param zone_load: ideal number of courier for each hour
        :param id_rider2time: information with courier id and pair (start_hour, end_hour)
        """
        self.__time_constraint = time_constraint - 1
        self.__zone_load = zone_load
        self.__id_rider2time = id_rider2time

    def _get_time_generator(self, start_hour: int, end_hour: int) -> Iterable:
        """
        :param start_hour: start hour of courier (possible)
        :param end_hour: end hour of courier (possible)
        :return:
        """
        possible_intervals = itertools.combinations(np.arange(start_hour, end_hour + 1), 2)
        constraints_intervals = itertools.filterfalse(lambda x: x[1] - x[0] < self.__time_constraint,
                                                      possible_intervals)
        return constraints_intervals

    def _get_time_and_id_generator(self) -> Iterable:
        it = itertools.product([0, 1], repeat=len(self.__id_rider2time))







        return it


    # def TODO: получить cum time


    def _check_courier_num(self) -> Union[None, int]:
        pass  #
        # TODO: Возвращать лучшее качество и синхронно записывать в sharable переменную в




    def __call__(self, *args, **kwargs):
        # 1. TODO Получить генератор всех параметров перебора
        # 2. Итерироваться по нему паралельно проверкой на необходимые условия
        pass




class GetSchedules:
    pass




if __name__ == "__main__":
    print("OLOLO")








