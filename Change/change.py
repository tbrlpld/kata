# -*- coding: utf-8 -*-

"""Small program to return the least number of coins for a given cent value."""

# TODO: Add user interaction or command line arguments. Both is possible.
#       When argument available on the command line, then use that.
#       If not arguments are given, start interactive mode.

# TODO: Package program and test on different computer.

from argparse import ArgumentParser
from typing import Dict, List
from pprint import pprint


class Coin(object):
    """
    Coin class to create coin objects.

    A coin can be created with a given name and value. Once the name and value
    have been defined, the name and value can not be changed
    """

    def __init__(self, name: str, cent_value: int):
        """Initialize a coin."""
        self._name = name
        self._cent_value = cent_value

    @property
    def name(self) -> str:
        """Name of the coin."""
        return self._name

    @property
    def value(self) -> int:
        """Value of the coin."""
        return self._cent_value

    def __repr__(self) -> str:
        """Define representation of a coin object when printed."""
        return "{0} ({1} cent(s))".format(self.name, self.value)


class ChangeMaker(object):
    """Class that calculates the change based on given cent value."""

    def __init__(self):
        """Create ChangeMaker object."""
        self._penny: Coin = Coin(name="penny", cent_value=1)
        self._nickel: Coin = Coin(name="nickel", cent_value=5)
        self._dime: Coin = Coin(name="dime", cent_value=10)
        self._quarter: Coin = Coin(name="quarter", cent_value=25)
        self._coins_unsorted: List[Coin] = [
            self._penny,
            self._nickel,
            self._dime,
            self._quarter,
        ]
        self.coins: List[Coin] = sorted(
            self._coins_unsorted,
            key=lambda coin: coin.value,
            reverse=True,
        )

    def change(self, cents: int) -> Dict[str, int]:
        """Return given cent value with the least number of coins."""
        coins_to_return: Dict[str, int] = {}

        target_value_of_coins: int = cents
        combined_value_of_coins: int = 0
        # Iterate through the coins starting with the largest
        for current_coin in self.coins:
            # Add coin if result still smaller than or equal to target
            while (
                combined_value_of_coins + current_coin.value
                <= target_value_of_coins
            ):
                if coins_to_return.get(current_coin.name) is None:
                    coins_to_return[current_coin.name] = 1
                else:
                    coins_to_return[current_coin.name] += 1
                combined_value_of_coins += current_coin.value

        return coins_to_return

    def display_change(self, cents: int) -> None:
        """Calculate and display change for given cent value."""
        change = self.change(cents)
        for coin in self.coins:
            count_of_coin = change.get(coin.name)
            if count_of_coin is not None:
                print("{0}: {1}".format(coin.name, count_of_coin))


argparser = ArgumentParser()
argparser.add_argument(
    "cents",
    type=int,
    help="Cent value to generate the change with the least number of coins.",
)

if __name__ == "__main__":
    args = argparser.parse_args()
    changemaker = ChangeMaker()
    changemaker.display_change(cents=args.cents)
