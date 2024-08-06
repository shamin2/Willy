# pet.py
import json

class Pet:
    def __init__(self):
        self.hunger = 50
        self.thirst = 50
        self.happiness = 50
        self.health = 100
        self.energy = 50
        self.boredom = 50  # Initialize boredom level

    def feed(self):
        self.hunger = max(0, self.hunger - 20)
        self.health = min(100, self.health + 5)

    def drink(self):
        self.thirst = max(0, self.thirst - 20)
        self.health = min(100, self.health + 5)

    def play(self):
        self.happiness = min(100, self.happiness + 10)
        self.energy = max(0, self.energy - 10)
        self.boredom = max(0, self.boredom - 20)

    def groom(self):
        self.happiness = min(100, self.happiness + 5)
        self.boredom = max(0, self.boredom - 5)

    def sleep(self):
        self.energy = min(100, self.energy + 20)
        self.health = min(100, self.health + 10)

    def save_state(self):
        with open('pet_state.json', 'w') as f:
            json.dump(self.__dict__, f)

    def load_state(self):
        try:
            with open('pet_state.json', 'r') as f:
                data = json.load(f)
                self.__dict__.update(data)
        except FileNotFoundError:
            pass
