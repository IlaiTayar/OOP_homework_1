class Person:

    def __init__(self, first_name, last_name, age, gender, married):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.married = married
        self.owned_animals = []

    def print_info(self):

        print(f" first_name: {self.first_name}"
              f"\n last_name: {self.last_name}"
              f"\n age: {self.age}"
              f"\n gender: {self.gender}"
              f"\n married: {self.married}"
              f"\n owned_animals: ")

        if len(self.owned_animals) == 0:
            print(" No animals found")
        else:
            for animal in self.owned_animals:
                print(f"({animal.type}, {animal.name})")

    def add_animal(self, animal):
        self.owned_animals.append(animal)

    def del_animal(self, animal):
        self.owned_animals.remove(animal)