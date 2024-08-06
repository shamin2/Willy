import json

class Pet:
    """
    The Pet class models a virtual pet with attributes and behaviors
    that simulate interactions with a real-life pet. It manages the pet's
    state, including hunger, thirst, happiness, health, energy, and boredom levels.
    """

    def __init__(self):
        """
        Initializes a new instance of the Pet class with default attribute values.
        """
        self.hunger = 50    # Hunger level of the pet (0-100)
        self.thirst = 50    # Thirst level of the pet (0-100)
        self.happiness = 50 # Happiness level of the pet (0-100)
        self.health = 100   # Health level of the pet (0-100)
        self.energy = 50    # Energy level of the pet (0-100)
        self.boredom = 50   # Boredom level of the pet (0-100)

    def feed(self):
        """
        Feeds the pet, reducing hunger and slightly increasing health.
        Ensures that hunger does not drop below 0 and health does not exceed 100.
        """
        self.hunger = max(0, self.hunger - 20)
        self.health = min(100, self.health + 5)

    def drink(self):
        """
        Gives the pet a drink, reducing thirst and slightly increasing health.
        Ensures that thirst does not drop below 0 and health does not exceed 100.
        """
        self.thirst = max(0, self.thirst - 20)
        self.health = min(100, self.health + 5)

    def play(self):
        """
        Plays with the pet, increasing happiness, reducing energy, and decreasing boredom.
        Ensures that happiness does not exceed 100, energy does not drop below 0,
        and boredom does not drop below 0.
        """
        self.happiness = min(100, self.happiness + 10)
        self.energy = max(0, self.energy - 10)
        self.boredom = max(0, self.boredom - 20)

    def groom(self):
        """
        Grooms the pet, slightly increasing happiness and reducing boredom.
        Ensures that happiness does not exceed 100 and boredom does not drop below 0.
        """
        self.happiness = min(100, self.happiness + 5)
        self.boredom = max(0, self.boredom - 5)

    def sleep(self):
        """
        Allows the pet to sleep, increasing energy and health.
        Ensures that energy and health do not exceed 100.
        """
        self.energy = min(100, self.energy + 20)
        self.health = min(100, self.health + 10)

    def save_state(self):
        """
        Saves the current state of the pet to a JSON file named 'pet_state.json'.
        This includes all attribute values of the pet.
        """
        with open('pet_state.json', 'w') as f:
            json.dump(self.__dict__, f)

    def load_state(self):
        """
        Loads the pet's state from the 'pet_state.json' file if it exists.
        Updates the current state with the loaded values. If the file is not found,
        it retains the initial state without making changes.
        """
        try:
            with open('pet_state.json', 'r') as f:
                data = json.load(f)
                self.__dict__.update(data)
        except FileNotFoundError:
            pass
