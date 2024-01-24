from data_structures.queue import Queue


class AnimalShelter:
    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()
        self.lizards = Queue()

    def enqueue(self, animal):
        if animal.species == "dog":
            self.dogs.enqueue(animal)
        elif isinstance(animal, Cat): #cool... CoPilot taught me the isinstance function
            self.cats.enqueue(animal)
        elif isinstance(animal, Lizard):
            self.lizards.enqueue(animal)
            self.lizards.dequeue()
            print("Just kidding, we don't accept lizards here")
        else:
            raise TypeError("We only accepts dogs and cats here... maybe lizards in the future")

    def dequeue(self, pref):
        if pref == "dog":
            return self.dogs.dequeue()
        elif pref == "cat":
            return self.cats.dequeue()
        else:
            return None


class Dog:
    def __init__(self, name="I need a name"):
        self.species = "dog"
        self.name = name


class Cat:
    def __init__(self, name="I need a name"):
        self.species = "cat"
        self.name = name


class Lizard:
    def __init__(self, name="I need a name"):
        self.species = "lizard"
        self.name = name
