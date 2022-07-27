class Doggy:

    num_of_dogs = 0
    birth_of_dogs = 0

    @classmethod
    def bark(cls):
        print('woo woo')
    
    def __init__(self, dog_name):
        self.dog_name = dog_name
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1
    
    @classmethod
    def get_status(cls):
        print(Doggy.birth_of_dogs, Doggy.num_of_dogs)

    def __del__(self):
        Doggy.num_of_dogs -= 1


Doggy.bark() # woo woo

dog1 = Doggy('뽀삐')
dog2 = Doggy('냥냥이')
dog3 = Doggy('멍멍이')
del dog1 # dog1 제거

Doggy.get_status() # 3 2