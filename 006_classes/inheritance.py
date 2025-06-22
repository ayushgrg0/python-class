# Inheritance

# instance == object


class Janawaar:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return ""


class Dog(Janawaar):
    def speak(self):
        return f"{self.name}, barks!!"


class Cat(Janawaar):
    def speak(self):
        return f"{self.name}, meows!!"


dog = Dog("Kale")
cat = Cat("Suri")

print(dog.speak())
print(cat.speak())


class Teacher:
    total_teacher = 0

    def __init__(self, name) -> None:
        self.name = name
        Teacher.total_teacher += 1

    @classmethod
    def get_total_teacher(cls):
        return cls.total_teacher


teacher1 = Teacher("Ram")
teacher2 = Teacher("Shyam")
teacher3 = Teacher("Hari")


print(Teacher.get_total_teacher())
