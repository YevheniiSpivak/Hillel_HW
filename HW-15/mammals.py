from animals import Animals


class Mammals(Animals):

    def __init__(self, name: str, age: int, gender: str):
        super().__init__(name, age, gender)

    def feed_offspring(self):
        return f'{self.name} feeds the offspring'
