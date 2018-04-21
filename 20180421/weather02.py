from random import choice
from typing import List


def forcast() -> object:
    possibilities: List[str] = ["sunny", "rain", "snow", "cloudy", "unknown"]
    return choice(possibilities)