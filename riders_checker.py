import itertools
import numpy as np

from typing import Union, Dict, Tuple, Iterable

from queue import Queue

from riders_combination_storage import RidersCombinationsStorage
from combinations_checker import CombinationsChecker


class RidersIterator:
    """
    """
    def __init__(self, riders_combinations_storage: RidersCombinationsStorage,
                 combinations_checker: CombinationsChecker):
        """
        :param riders_combinations_storage:
        :param combinations_checker:
        """
        self.__combination_deque = Queue()  # очередь для обхода riders
        self.__riders_combinations_storage = riders_combinations_storage
        self.__combinations_checker = combinations_checker

        self.__ids = None  # все riders
        self.__combinations = None  # Наборы, которые нет смысла проверять
        self.__combination_deque_init()

    def __combination_deque_init(self):
        self.__ids = frozenset(self.__riders_combinations_storage.ids)
        [(self.__combination_deque.put(id), ()) for id in self.__ids]

    def put_combinations(self, id: Tuple):  # добавлеяет элмент в очередь и в self._riders_combinations_storage
        """
        :param id:
        :return:
        """
        pass

        # инвариантность порядка (r1, r2, r3) & (r3, r2, r1)


        # если (r1, r2, r3) не подошел  то и (r1, r2, r4, r3) не подойдет !!!







    def __call__(self):
        while not self.__combination_deque.empty():
            pair_id = self.__combination_deque.get()
            # получение матрицы вохможных графиков курьеров для последующей проверки
            intervals_matrix = self.__riders_combinations_storage.get_combinations(*pair_id)

            # 1. Проверка данной комбинации и отсеивание тех, которые не подходят
            row_indexes, time_borders = self.__combinations_checker(intervals_matrix)

            # 2. добавлние в очередь
            new_id = (*pair_id[0], *pair_id[1])
            self.put_combinations(new_id)

            # 3. Обновить словарь
            self.__riders_combinations_storage.set_combinations(pair_id[0], pair_id[1], row_indexes, time_borders)

        # return возврат лучшей комбинации

    # Дешево сделать мультитпроцессинг на данной очереди ???
