from enum import Enum


class SiteBatteryControlCommand(str, Enum):
    CHARGE = "charge"
    DISCHARGE = "discharge"
    IDLE = "idle"

    def __str__(self) -> str:
        return str(self.value)
