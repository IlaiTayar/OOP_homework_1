from clases.person import Person
from clases.animal import Animal
from clases.ract_mkr import  Ract_mkr

if __name__ == '__main__':
    #answer 1.

    person_1 = Person("ilai", "tayar", 24, "male", False)
    person_2 = Person("ben", "ben_moshe", 30, "male", True)
    person_3 = Person("roze", "tayar", 20, "female", False)

    print("--------------------------")

    print(type(person_1))
    print(type(person_2))
    print(type(person_3))

    print("--------------------------")

    print(getattr(person_1, "married"))
    setattr(person_1, "married", True)
    print(getattr(person_1, "married"))

    print("--------------------------")

    person_2.married = False
    print(person_2.married)

    print("--------------------------")


    #answer 2

    animal_1 = Animal("cat", "chubzi", 4, "male", "salmon")
    animal_2 = Animal("dog", "bullie", 4, "female", "steak")
    animal_3 = Animal("hamster", "robbie", 4, "male", "hamster_food")

    animal_1.print_info()
    print("--------------------------")
    animal_2.print_info()
    print("--------------------------")
    animal_3.print_info()
    print("--------------------------")
    owner_1 = Person("ilai", "tayar", 24, "male", None, )
    owner_2 = Person("ben", "ben_moshe", 30, "male", None, )
    owner_3 = Person("roze", "tayar", 20, "female", None, )

    owner_1.add_animal(animal_1)
    owner_1.add_animal(animal_2)
    owner_2.add_animal(animal_3)

    owner_1.print_info()
    print("--------------------------")
    owner_2.print_info()
    print("--------------------------")
    owner_3.print_info()
    print("--------------------------")
    owner_1.del_animal(animal_2)
    owner_1.print_info()
    print("--------------------------")


    #answer 3
    ract_1 = Ract_mkr(15, 9)
    ract_1.print_ract()
    print("--------------------------")
    print(ract_1.get_area())
    print("--------------------------")



