class Animals:

    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return (f'{self.__class__.__name__}: {self.name}'
                f'\nAge: {self.age}'
                f'\nGender: {self.gender}')

    def move(self):
        return f'{self.name} moving'

    def eat(self):
        return f'{self.name} eating'

    def sleep(self):
        return f'{self.name} sleeping'

    def reproduces(self):
        if self.age < 3:
            return f'{self.name} is too small to reproduce'
        return f'{self.name} began to reproduce'
