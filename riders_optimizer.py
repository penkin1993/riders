import itertools

import pandas as pd
import numpy as np

from typing import Union, Dict, Tuple, Iterable, Hashable

from riders_combinations_checker import RidersCombinationsChecker
from riders_combination_storage import RidersCombinationsStorage
from riders_iterator import RidersIterator


class RidersOptimizer:
    """
    """
    def __init__(self, zones: pd.DataFrame, riders: pd.DataFrame, start_hour: int = 6):
        """
        :param zones:
        :param riders:
        :param start_hour:
        """
        self.__zones = zones
        self.__riders = riders

        self.__start_hour = start_hour

    def count_zone(self, zone_id: Hashable) -> pd.DataFrame:
        """
        :param zone_id:
        :return:
        """
        print(f" zone_id = {zone_id} optimization processing")
        riders_in_zones = self.__zones.loc[self.__zones.index == zone_id].values[0]
        poss_riders = self.__riders.loc[self.__riders.zone_id == zone_id, ["start_hour", "end_hour"]]
        poss_riders = poss_riders - self.__start_hour
        id_rider2time = {ind: tuple(poss_riders.loc[ind]) for ind in poss_riders.index}

        rcc = RidersCombinationsChecker(riders_in_zones)
        rcs = RidersCombinationsStorage(id_rider2time=id_rider2time,
                                        working_duration=riders_in_zones.shape[0],
                                        working_time_constraint=3)

        ri = RidersIterator(riders_combinations_storage=rcs,
                            riders_combinations_checker=rcc)

        rider_id, res_time, _ = ri()
        pd_res = pd.DataFrame(res_time, index=rider_id, columns=["start_hour", "end_hour"])
        pd_res = pd_res + self.__start_hour
        pd_res.index.name = "rider_id"
        pd_res["zone_id"] = zone_id
        return pd_res

    def __call__(self):
        """
        :return:
        """
        return pd.concat([self.count_zone(zone_id) for zone_id in np.unique(self.__zones.index)], axis=0)















