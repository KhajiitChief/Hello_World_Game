class Pet():
    def __init__(self, **kwargs):
        self.name = kwargs["pet_name"] if "pet_name" in kwargs else "You're pet does not have a name..."
        self.age = kwargs["pet_age"] if "pet_age" in kwargs else "You're pet does not have a name..."
        self.breed = kwargs["pet_breed"] if "pet_breed" in kwargs else "You're pet is unidentifiable..."
        print(self.__dict__)
    def sort_pet(self):
        if self.breed == "cat":
            print(f"You're cat may be {self.age}, but they still have 9 lives!!!")
        elif self.breed == "dog":
            print("Your pet can be tough to train, but will be loyal for life...")
        elif self.breed == "rock":
            print("Your pet is useless...")
        else:
            print("Your pet cannot be sorted...")

pet1 = Pet(pet_name= input("what is your pet's name???"), pet_age= input("What is your pet's age???"),
           pet_breed= input("What is your pet's breed???").lower())
print(pet1.sort_pet())