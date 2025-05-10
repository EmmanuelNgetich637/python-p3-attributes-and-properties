#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name=None, breed="Pug"):
        self._name = None
        self._breed = None

        # Validate and set name
        if name is not None:
            if isinstance(name, str) and 1 <= len(name) <= 25:
                self._name = name
            else:
                print("Name must be string between 1 and 25 characters.")
                self._name = "None"
        
        # Validate and set breed
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")
            self._breed = "None"

    @property
    def name(self):
        return self._name

    @property
    def breed(self):
        return self._breed
