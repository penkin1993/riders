import itertools
import numpy as np

from typing import Union, Dict, Tuple, Iterable


# TODO: Защита от рассчета дважды (id1 id2) (id2 id1)

# TODO: Init (вычисление лоса) каждого курьера по отдельности


class RidersIterator:
    """
    TODO: Docstring
    """
    def __init__(self):
        pass



    def _get_courier_iterator(self) -> Iterable:
        it = itertools.product([0, 1], repeat=len(self.__id_rider2time))
        # TODO: Заменить на очередь !!!!
        # TODO: Данная очерредб должна быть приватная, но релаизовывать публичные методы манипуляциии с ней классом
        # Courier Checker







    # def Составление новых различных комбинаций различных комбинаций







    # def Помещение их в очередь





# class В отдельный класс ??????

    # def  Проверка подходящего и решение помещать в очередь или нет


    # def паралельное вычисление наборов, выбор всех по два или три и запуска их параллельно ???





