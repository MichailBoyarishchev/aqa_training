class Person:

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def get_up(self):
        print(self.sex, self.name, "gets up")

    def Sit_down(self):
        print(self.sex, self.name, "sits down")

    def Lie_down(self):
        print(self.sex, self.name, "lies down")


class Employee(Person):
    def __init__(self, name, sex, position, salary):
        super().__init__(name, sex)
        self.salary = salary
        self.position = position

    def go_work(self):
        print(self.position, "with a salary of $", self.salary, "goes to work")

    def log_work(self):
        print(self.position, "with a salary of $", self.salary, "logs time")

    def full_getUp(self):
        Person.get_up(self)
        print("working in position", self.position, "with a salary of $", self.salary)

    def full_sitDown(self):
        Person.Sit_down(self)
        print("working in position", self.position, "with a salary of $", self.salary)

    def full_lieDown(self):
        Person.Lie_down(self)
        print("working in position", self.position, "with a salary of $", self.salary)


Roma = Employee("Roma", "man", "Lead", 3000)
Roma.get_up()
Roma.Sit_down()
Roma.log_work()
Roma.go_work()
Roma.Lie_down()
Irina = Person("Irina", "woman")
Irina.Lie_down()
Roma.full_getUp()
Roma.full_lieDown()
Roma.full_sitDown()
