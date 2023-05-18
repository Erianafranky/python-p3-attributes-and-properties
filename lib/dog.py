#!/usr/bin/env python3

"""
Define a name property for your Dog class. The name must be of type str and between 1 and 25 characters.
If the name is invalid, the setter method should print() "Name must be string between 1 and 25 characters."
Define a breed property for your Dog class.
If the breed is invalid, the setter method should print() "Breed must be in list of approved breeds." 
"""

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
    def __init__(self, name='Luna', breed='Corgi'):
        self.name = name
        self.breed = breed

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if (type(name) == str) and (1 <= len(name) <= 25):
            self._name = name.title()
        else:
            print('Name must be string between 1 and 25 characters.')
    name = property(get_name, set_name)

    def get_breed(self):
        return self._breed
    
    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")
    breed = property(get_breed, set_breed)


