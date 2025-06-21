# combination of behaviour and attributes is encapsulation


class Student:
    college = "ICP"  # class variable

    def __init__(self, name):
        self.name = name
        # self.college = "KMA"     (Overriding the college name!)

    def introduction(self):
        return f"My name is {self.name}. I study in {self.college}."


student1 = Student("Ayush")
student2 = Student("Ram")

print(student1.introduction())
print(student2.introduction())
