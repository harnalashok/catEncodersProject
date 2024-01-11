# File: xyz.py

class Animal:
    """
    A simple class representing an animal.

    Attributes:
    - name (str): The name of the animal.
    - species (str): The species of the animal.

    Methods:
    - make_sound(): Prints a generic sound that the animal makes.
    - move(): Prints a message indicating the animal is moving.

    Example usage:
    >>> lion = Animal(name="Leo", species="Lion")
    >>> lion.make_sound()
    Leo the Lion says: Roar!
    >>> lion.move()
    Leo the Lion is moving.
    """

    def __init__(self, name, species):
        """
        Initializes an instance of the Animal class.

        Parameters:
        - name (str): The name of the animal.
        - species (str): The species of the animal.
        """
        self.name = name
        self.species = species

    def make_sound(self):
        """Prints a generic sound that the animal makes."""
        print(f"{self.name} the {self.species} says: Roar!")

    def move(self):
        """Prints a message indicating the animal is moving."""
        print(f"{self.name} the {self.species} is moving.")
