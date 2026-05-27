class Animal:

    def __init__(self, type, name, age, gender, favorite_food):
        self.type = type
        self.name = name
        self.age = age
        self.gender = gender
        self.favorite_food = favorite_food


    def print_info(self):

        print(f" type: {self.type}"
              f"\n name: {self.name}"
              f"\n age: {self.age}"
              f"\n gender: {self.gender}"
              f"\n favorite food: {self.favorite_food}")