import itertools
import numpy as np

from typing import Union, Dict, Tuple, Iterable

from queue import Queue

from riders_iterator import RidersCombinationsStorage
from combinations_checker import CombinationsChecker


class RidersIterator:
    """
    TODO: Docstring
    """
    def __init__(self, riders_combinations_storage: RidersCombinationsStorage,
                 combinations_checker: CombinationsChecker):
        """
        :param riders_combinations_storage:
        """
        self.__combination_deque = Queue()  # очередь для обхода riders
        self.__riders_combinations_storage = riders_combinations_storage
        self.__combinations_checker = combinations_checker

        self.__ids = None  # все riders
        self.__combinations = None  # Наборы, которые нет смысла проверять
        self.__combination_deque_init()

    def __combination_deque_init(self):
        self.__ids = frozenset(self.__riders_combinations_storage.ids)
        [(self.__combination_deque.put(id), ) for id in self.__ids]




    def add_combinations(self):  # добавлеяет элмент в очередь и в self._riders_combinations_storage
        pass

        # инвариантность порядка (r1, r2, r3) & (r3, r2, r1)


        # если (r1, r2, r3) не подошел  то и (r1, r2, r4, r3) не подойдет !!!









    def __call__(self):  # точка входа в программу. Запуск основного цикла
        while not self.__combination_deque.empty():
            combination = self.__combination_deque.get()  # tuple

            # TODO: Нужна матрица (сумма из __riders_combinations_storage) и добавить с него тривальный случай

            # 1. Проверка данной комбинации и отсеивание тех, которые не подходят
            row_indexes, time_borders = self.__combinations_checker(combination)

            # 2. добавлние в очередь

            # 3. обновлять словарь при необходимости


        # return возврат лучшей комбинации











    # TODO: Как рабоатет очередь. Можно ли дешево сделать мультитпроцессинг ???




