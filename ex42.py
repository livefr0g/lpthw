# Animal is-a object
class Animal(object):

    def eat(self):
        print "Eating ..."

# is-a
class Dog(Animal):

    def __init__(self, name):
        # has-a
        self.name = name

    def bark(self):
        print "Ruff! rufffff ruff!"

# is-a
class Cat(Animal):

    def __init__(self, name):
        # has-a
        self.name = name

# is-a
class Person(object):

    def __init__(self, name):
        # has-a
        self.name = name

        # Person has a kind of pet
        self.pet = None

# is-a
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        # has-a
        self.salary = salary

# is-a
class Fish(object):
    pass

# is-a
class Salmon(Fish):
    pass

# is-a
class Halibut(Fish):
    pass


# rover is-a Dog
rover = Dog("Rover")

# satan is-a Cat
satan = Cat("Satan")

# mary is-a Person
mary = Person("Mary")

# has-a
mary.pet = satan
satan.eat()
try:
    satan.bark()
except AttributeError:
    print "Cat's can't bark!" 

# is-a
frank = Employee("Frank", 120000)

# has-a
frank.pet = rover
rover.eat()
rover.bark()

# is-a
flipper = Fish()

# is-a
crouse = Salmon()

# is-a
harry = Halibut()