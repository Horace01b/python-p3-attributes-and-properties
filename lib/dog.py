#!/usr/bin/env python3
class Dog:
    approved_breeds = [
        "Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle",
        "French Bulldog", "Pug", "Pointer"
    ]

    def __init__(self, name="Fido", breed="Mutt"):
        # First try to set the name
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self.name = name
            # Only set breed if name was valid
            self.breed = breed
        else:
            print("Name must be string between 1 and 25 characters.")
            self._name = None  # optional: keep attribute defined

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value in self.approved_breeds:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")
