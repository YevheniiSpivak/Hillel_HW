class Employee:

    def __init__(self, name: str, age: int, position: str, gender: str, salary: int):
        self.position = position
        self.name = name
        self.age = age
        self.gender = gender
        self.salary = salary

    def into(self):
        print(f'Name: {self.name}\n'
              f'Age: {self.age}\n'
              f'Position: {self.position}\n'
              f'Salary: {self.salary}$\n')

    def change_position(self, position: str):
        self.position = position

    def change_salary(self, salary: int):
        self.salary = salary

    def grows_up(self, ages: int):
        self.age = self.age + ages


bill = Employee('Bill', 27, 'junior automation', 'male', 1000)

bill.into()
bill.change_position('middle automation')
bill.change_salary(1500)
bill.grows_up(1)
bill.into()
