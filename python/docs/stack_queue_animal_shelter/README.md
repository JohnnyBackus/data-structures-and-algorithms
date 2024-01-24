# Stack-Queue-Animal-Shelter

First-in, First out Animal Shelter.

## Feature Tasks

- Create a class called AnimalShelter which holds only dogs and cats.
- The shelter operates using a first-in, first-out approach.
- Implement the following methods:
  - enqueue
    - Arguments: animal
      - animal can be either a dog or a cat object.
      - It must have a species property that is either "cat" or "dog"
      - It must have a name property that is a string.
  - dequeue
    - Arguments: pref
      - pref can be either "dog" or "cat"
    - Return: either a dog or a cat, based on preference.
      - If pref is not "dog" or "cat" then return null.

## Whiteboard Process

[!Whiteboard Diagram](cc12_whiteboard.jpg)

## Approach & Efficiency

**What approach did you take? Why?**

*I had to stare at the tests for a while to have any idea of where to start and to better understand the instructions, but eventually figuered as follows...*

- Using a FIFO approach means that a single Queue is not sufficient to hold dogs and cats if we are expected to be able to choose to dequeue by species/preference
  - We will need to instantiate separate queues for dogs & cats inside of the AnimalShelter class
  - The enqueue method will use a conditional to screen by species
    - it will then use the previously-created Queue class method to populate the appropriate dog or cat queue
  - The dequeue method will use a conditional to screen by pref/species
    - it will then use the previously-created Queue class method to dequeue the appropriate dog or cat queue and return the animal
    - an else statement will be used to return None for any pref argument that is not "cat" or "dog"

**What is the Big O space/time for this approach?**

>*These methods have a space time complexity of O(1). The size of either dog or cat queue does not increase the number of steps needed to complete the operation.*

## Resources

- [CodeFellows Technical Whiteboarding Guidelines](https://codefellows.github.io/common_curriculum/challenges/code/whiteboarding)

- used GitHub copilot helped with syntax errors. It also taught me the isinstance method.
  - `isinstance(animal, Dog)` can replace `if animal.species == "dog"` and seem more specific to this application.
    - I used both to verify they both work.

## Solution

'''
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
'''
