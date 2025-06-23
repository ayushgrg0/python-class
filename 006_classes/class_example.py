

class Animal:
    def __init__(self, name):  # self paxi aauni object ko lagi thau xoddeko, same object lai refer gareko
        self.name = name

    def intro(self):
        print(f'My name is {self.name}')
        print("Inside the intro")
        print(self)
        print("Inside the intro")


a = Animal("Coco")
a.intro()
print("Called outside the class")
print(a)
print("Called outside the class")

# __init__
# __str__
# __repr__

