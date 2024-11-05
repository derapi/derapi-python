from enum import Enum


class SummaryLevel(str, Enum):
    DAY = "day"
    HOUR = "hour"
    MONTH = "month"
    VALUE_3 = "15mins"

    def __str__(self) -> str:
        return str(self.value)
