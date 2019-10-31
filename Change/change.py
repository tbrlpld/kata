# -*- coding: utf-8 -*-

"""Small program to return the least number of coins for a given cent value."""



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
    def name(self):
        """Name of the coin."""
        return self._name

    @property
    def value(self):
        """Value of the coin."""
        return self._cent_value

    def __repr__(self):
        return "{0} ({1} cent(s))".format(self.name, self.value)


PENNY = Coin(name="penny", cent_value=1)
NICKLE = Coin(name="nickel", cent_value=5)
DIME = Coin(name="dime", cent_value=10)
QUARTER = Coin(name="quarter", cent_value=25)

COINS = sorted(
    [PENNY, NICKLE, DIME, QUARTER], key=lambda coin: coin.value, reverse=True)


def change(cents: int):
    """Return the least number of coins for the given cent value."""
    coins_to_return = {}

    target_value_of_coins = cents
    combined_value_of_coins = 0
    # Iterate through the coins starting with the largest
    for coin in COINS:
        current_coin = coin
        # Add coin if result still smaller than or equal to target
        while (
            combined_value_of_coins + current_coin.value
            <= target_value_of_coins
        ):
            if coins_to_return.get(coin.name) is None:
                coins_to_return[current_coin.name] = 1
            else:
                coins_to_return[current_coin.name] += 1
            combined_value_of_coins += current_coin.value

    return coins_to_return
