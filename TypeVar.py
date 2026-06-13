from typing import TypeVar, Generic, Callable

T = TypeVar('T')


# 1
class PriorityQueue(Generic[T]):

    def __init__(self, priority_func: Callable[[T], int]):
        self.priority_func = priority_func
        self.elements = []
    
    def push(self, item: T):
        self.elements.append(item)

    def pop(self) -> T:

        best = self.elements[0]

        for element in self.elements:
            if self.priority_func(element) > self.priority_func(best):
                best = element  
        
        self.elements.remove(best)

        return best
    
q = PriorityQueue[int](lambda x: x)

q.push(10)
q.push(5)
q.push(20)

print(q.pop())  # 20
print(q.pop())  # 10
print(q.pop())  # 5

# 2

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def bark(self):
        return "Woof!"

class Cat(Animal):
    def meow(self):
        return "Meow!"

dog1 = Dog("собака")
cat1 = Cat("кошка")

#copyanimals
dogs = [
    Dog("собака"),
]

animals = [
    Cat("кошка")
]

def copyAnimals(src, dst):

    for dog in src:
        dst.append(dog)

copyAnimals(dogs, animals)


for animal in animals:
    print(animal.name)

#fillwitcats

animals = [
    Dog("Бобик")
]

[
    Cat("Кот1"),
    Cat("Кот2"),
    Cat("Кот3")
]

def fillWithCats(dst):

    dst.clear()

    dst.append(Cat("Кот1"))
    dst.append(Cat("Кот2"))
    dst.append(Cat("Кот3"))

fillWithCats(animals)

#safetransfer
dogs = [
    Dog("Бобик"),
    Dog("Шарик")
]

animals = []

def safeTransfer(src, dst):
    for element in src:
            dst.append(element)
safeTransfer(dogs, animals)
