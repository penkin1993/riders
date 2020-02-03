import itertools
import numpy as np

from typing import Union, Dict, Tuple, Iterable

from collections import deque

from riders_iterator import RidersCombinationsStorage


# TODO: Защита от рассчета дважды (id1 id2) (id2 id1)

# TODO: Init (вычисление лоса) каждого курьера по отдельности


class RidersIterator:
    """
    TODO: Docstring
    """
    def __init__(self, riders_combinations_storage):
        self._combination_deque = deque()
        self._riders_combinations_storage = riders_combinations_storage




    def combination_deque_init(self):
        pass  # инициализация исходной очереди





    def __next__(self):  # возвращает следующий элемент из очереди
        pass






    def add(self):  # добавлеяет элмент в очередь и в self._riders_combinations_storage
        pass




    def __call__(self): # точка входа в программу. Запуск основного цикла
        pass







class CombinationsChecker:
    """
    Класс для проверки комбинаций на удовлеторениме требований !!!!
    """
    # Хранить лучший набор здесь ???

    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):  # Проверка подходящего и решение помещать в очередь или нет
        pass


    # def паралельное вычисление наборов, выбор всех по два или три и запуска их параллельно ???





