import itertools
import time

from queue import Queue
from typing import Tuple


from riders_combination_storage import RidersCombinationsStorage
from riders_combinations_checker import RidersCombinationsChecker


class RidersIterator:
    """
    Класс для обхода в ширину всех комбинаций курьеров
    """
    def __init__(self, riders_combinations_storage: RidersCombinationsStorage,
                 riders_combinations_checker: RidersCombinationsChecker):
        """
        :param riders_combinations_storage:
        :param riders_combinations_checker:
        """
        self.__combinations_queue = Queue()  # очередь для обхода riders
        self.__riders_combinations_storage = riders_combinations_storage
        self.__riders_combinations_checker = riders_combinations_checker

        self.__ids = None  # все riders
        self.__checked_combinations = set()  # Наборы, которые нет смысла проверять
        self.__combination_queue_init()

    def __combination_queue_init(self):
        self.__ids = set(x[0] for x in self.__riders_combinations_storage.ids)
        [self.__combinations_queue.put(((id, ), ())) for id in self.__ids]

    def __add_in_checked_combinations(self, id: Tuple):
        """
        :param id:
        :return:
        """
        # если (r1, r2, r3) не подошел  то и (r1, r2, r4, r3) не подойдет !!!
        id = set(id)
        rest_ids = self.__ids - id  # дополнение возможных ключей к текущему
        for i in range(1, len(rest_ids) + 1):
            for comb in itertools.combinations(rest_ids, i):
                self.__checked_combinations.add(frozenset((*id, *comb)))

    def __put_combinations(self, id: Tuple):  # добавлеяет элемент в очередь и в self._riders_combinations_storage
        """
        :param id:
        :return:
        """
        poss_ids = self.__ids - set(id)  # Все возможные продолжения
        for poss_id in poss_ids:
            add_id = set(id)
            add_id.add(poss_id)
            add_id = frozenset(add_id)
            if add_id not in self.__checked_combinations:
                # проверка инвариантности порядка (r1, r2, r3) & (r3, r2, r1)
                self.__checked_combinations.add(add_id)
                self.__combinations_queue.put((id, (poss_id, )))

    def __call__(self):
        """
        :return:
        """
        counter = 0
        t = time.time()

        while not self.__combinations_queue.empty():
            pair_id = self.__combinations_queue.get()

            counter += 1
            if not counter % 10:
                print(f" time_dif = {time.time() - t}, {len(pair_id[0]) + 1}")
                t = time.time()
            # получение матрицы возможных графиков курьеров для последующей проверки
            intervals_matrix, not_duplicate_index = self.__riders_combinations_storage.get_combinations(*pair_id)

            # 1. Проверка комбинаций и отсеивание тех, которые не подходят
            # ts1 = time.time()
            row_indexes, intervals_matrix, loss = self.__riders_combinations_checker(intervals_matrix)
            # ts2 = time.time()
            # print(ts2 - ts1)

            new_id = (*pair_id[0], *pair_id[1])

            if len(row_indexes) == 0:
                self.__add_in_checked_combinations(new_id)
            else:
                self.__put_combinations(new_id)
                # обновить миниум
                self.__riders_combinations_storage.best_combination = (new_id, row_indexes, loss)
                # 3. Обновить словарь
                self.__riders_combinations_storage.set_combinations(new_id, not_duplicate_index, row_indexes,
                                                                    intervals_matrix)

        return self.__riders_combinations_storage.best_combination

    # TODO: Добавить тесты !!!!
