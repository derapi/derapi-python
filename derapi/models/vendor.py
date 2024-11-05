from enum import Enum


class Vendor(str, Enum):
    ENPHASE = "enphase"
    ENPHASEVPP = "enphasevpp"
    SMA = "sma"
    SMASBOX = "smasbox"
    SOLAREDGE = "solaredge"
    SOLIS = "solis"
    TESLA = "tesla"
    VIRTUAL = "virtual"

    def __str__(self) -> str:
        return str(self.value)
