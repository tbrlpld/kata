# -*- coding: utf-8 -*-

"""Small program to return the least number of coins for a given cent value."""

# TODO: Package program and test on different computer.

from argparse import ArgumentParser
from typing import Dict, List


class Coin(object):
    """
    Coin class to create coin objects.

    A coin can be created with a given name and value. Once the name and value
    have been defined, the name and value can not be changed
    """

    def __init__(self, name: str, face_value: int):
        """Initialize a coin."""
        self._name = name
        self._face_value = face_value

    @property
    def name(self) -> str:
        """Name of the coin."""
        return self._name

    @property
    def face_value(self) -> int:
        """Value of the coin."""
        return self._face_value

    def __repr__(self) -> str:
        """Define representation of a coin object when printed."""
        return "{0} ({1} cent(s))".format(self.name, self.face_value)


class CoinStack(Coin):
    """Class to represent a stack/set of coins."""

    def __init__(self, name: str, face_value: int, count: int = 0):
        """Initialize a CoinStack, by default the count is 0."""
        super().__init__(name=name, face_value=face_value)
        self.count: int = count

    @property
    def total_value(self):
        """Return combined cent value of the coins in the set."""
        return self.count * self.face_value

    def add_one(self):
        """Increase the count of these coins by one."""
        self.count += 1


class Change(object):
    """Class to hold state of change."""

    def __init__(self):
        """Create Change object."""
        self.pennies: CoinStack = CoinStack(name="penny", face_value=1)
        self.nickels: CoinStack = CoinStack(name="nickel", face_value=5)
        self.dimes: CoinStack = CoinStack(name="dime", face_value=10)
        self.quarters: CoinStack = CoinStack(name="quarter", face_value=25)

        coins_unsorted: List[Coin] = [
            self.pennies,
            self.nickels,
            self.dimes,
            self.quarters,
        ]
        self._coins_sorted_by_face_value: List[Coin] = sorted(
            coins_unsorted,
            key=lambda coin: coin.face_value,
            reverse=True,
        )

    @property
    def total_value(self):
        """Return the total value of the all coins included in the change."""
        return (
            self.pennies.total_value
            + self.nickels.total_value
            + self.dimes.total_value
            + self.quarters.total_value
        )

    @property
    def coins_sorted_by_face_value(self):
        """Return the coins sorted by face value."""
        return self._coins_sorted_by_face_value

    def display(self):
        """Display the current state of the change."""
        for coin in self.coins_sorted_by_face_value:
            if coin.count != 0:
                print("{0}: {1}".format(coin.name, coin.count))


class ChangeMaker(object):
    """Class that to hold logic to generate the change."""

    def __init__(self):
        """Create ChangeMaker object."""
        self.change = Change()

    def calc_change(self, cents: int) -> Change:
        """Generate the given cent value with the least number of coins."""
        target_value_of_coins: int = cents
        # Iterate through the coins starting with the largest
        for current_coin in self.change.coins_sorted_by_face_value:
            # Add coin if result still smaller than or equal to target
            while (
                self.change.total_value + current_coin.face_value
                <= target_value_of_coins
            ):
                current_coin.add_one()
        return self.change

    def get_change(self, cents: int) -> Dict[str, int]:
        """
        Return change as a dictionary.

        Coin names as keys and counts as values. Only coins with a count larger
        than 0 are included. If a coin is not included in the change (it has
        count 0) the coin name will not be available in the keys,
        """
        self.calc_change(cents)
        coins_to_return: Dict[str, int] = {}
        for coin in self.change.coins_sorted_by_face_value:
            if coin.count != 0:
                coins_to_return[coin.name] = coin.count
        return coins_to_return

    def display_change(self, cents: int) -> None:
        """Calculate and display change for given cent value."""
        self.calc_change(cents)
        self.change.display()


class App(object):
    """Class to hold the app logic."""

    def __init__(self):
        """Create an app instance."""
        self.argparser = ArgumentParser()
        self.argparser.add_argument(
            "cents",
            type=int,
            nargs="?",
            default=0,
            help="Cent value to generate the change for.",
        )

        self.changemaker = ChangeMaker()

    def get_user_input(self, cents: int = 0):
        """Get user input for cents."""
        while cents == 0:
            user_input = input(
                "Please enter a cent value to generate the change for: ",
            )
            try:
                cents = int(user_input)
            except ValueError:
                print("You can only enter integer cent value.")
        return cents

    def run(self):
        """Run the application."""
        args = self.argparser.parse_args()
        cents = args.cents
        if cents == 0:
            cents = self.get_user_input()
        self.changemaker.display_change(cents)


if __name__ == "__main__":
    app = App()
    app.run()
