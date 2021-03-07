class BaseAnimal:
    def __init__(self, name, age, mass, fly=False):
        self.name = name
        self.age = age
        self.mass = mass
        self.fly = fly

    def greet(self):
        
        print(f"""
        Hi humans, I'm {self.name}, I'm {self.age} years old and
        my mass is {self.mass}
        """)
        
        if self.fly:
            print("By the way I can fly :)")

class Pigeon(BaseAnimal):
    def __init__(self, name, age, mass, fly=True):
        super().__init__(name, age, mass, fly)

P1 = Pigeon("Julius", 4, 0.3)

P1.greet()