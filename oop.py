from abc import ABC, abstractmethod

# 1 задание - инкапсуляция 

class Person:
    def __init__(self) -> None:
        self.__age = None

    def set_age(self, age: int):
        if age >= 0:
            self.__age = age
        else:
            raise ValueError("возраст не может быть отрицательным")

    def get_age(self):
        return self.__age
    

"""
    p = Person()
    p.set_age(25)
    print(p.get_age()) # Вывод: 25
    p.set_age(-5) # ValueError: возраст не может быть отрицательным (использовал raise)
"""


# 2 задание - Наследование

class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def speak(self) -> str:
        return "i am am animal"

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def speak(self) -> str:
        return "Woof"

class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def speak(self) -> str:
        return "Meow"
    
"""
    dog = Dog("Buddy")
    cat = Cat("Kitty")
    print(dog.name, dog.speak()) # Вывод: Buddy Woof
    print(cat.name, cat.speak()) # Вывод: Kitty Meow
"""


# 3 задание - Полиморфизм

class Vehicle:
    def __init__(self) -> None:
        ...
    
    def move(self) -> str:
        return "Vehicle is moving"
    

class Car(Vehicle):
    def __init__(self) -> None:
        super().__init__()

    def move(self) -> str:
        return "Car is driving"
    
class Bicycle(Vehicle):
    def __init__(self) -> None:
        super().__init__()

    def move(self) -> str:
        return "Bicycle is pedaling"
    

def move(cls):
    try:
        return cls.move()
    except:
        return "проверьте что у класса, котрый вы передали, есть метод move()"

"""
    car = Car()
    bike = Bicycle()
    print(move(car)) # Вывод: Car is driving
    print(move(bike)) # Вывод: Bicycle is pedaling
"""


# 4 задание - Абстракция 

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        ...
    
class Rectangle(Shape):
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    
    def area(self) -> float:
        return self.x * self.y
    
class Circle(Shape):
    def __init__(self, r) -> None:
        self.r = r

    def area(self) -> float:
        return 3.14 * (self.r**2)

"""
    rect = Rectangle(10, 5)
    circle = Circle(7)
    print(rect.area()) # Вывод: 50
    print(circle.area()) # Вывод: 153.86
"""