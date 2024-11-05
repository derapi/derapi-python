from enum import Enum


class BatteryMode(str, Enum):
    BACKUP = "Backup"
    SAVINGS = "Savings"
    SELF_CONSUMPTION = "Self Consumption"

    def __str__(self) -> str:
        return str(self.value)
