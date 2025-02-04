#!/usr/bin/env python3

from .hash_table import HashTable


class QuadraticProbing(HashTable):
    """
    Basic Hash Table example with open addressing using Quadratic Probing
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _collision_resolution(self, key, data=None):
        i = 1
        new_key = self.hash_function(key + i**2)

        while self.values[new_key] is not None and self.values[new_key] != key:
            i += 1
            new_key = (
                None
                if self.balanced_factor() >= self.lim_charge
                else self.hash_function(key + i**2)
            )


            if new_key is None:
                break

        return new_key
