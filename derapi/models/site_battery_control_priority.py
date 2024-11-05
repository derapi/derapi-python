from enum import Enum


class SiteBatteryControlPriority(str, Enum):
    B = "B"
    GRID = "Grid"
    LOAD = "Load"
    PV = "PV"

    def __str__(self) -> str:
        return str(self.value)
