from mammals import Mammals


class Predators(Mammals):
    def __init__(self, name: str, age: int, gender: str):
        super().__init__(name, age, gender)

    def hunt(self):
        return f'{self.name} hunting'


lion = Predators(name='Simba', age=3, gender='male')

print(lion)
print(lion.move())
print(lion.eat())
print(lion.sleep())
print(lion.feed_offspring())
print(lion.reproduces())
