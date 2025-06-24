

# class Animal:
#     def __init__(self, name):  # self paxi aauni object ko lagi thau xoddeko, same object lai refer gareko
#         self.name = name

#     def intro(self):
#         print(f'My name is {self.name}')
#         print("Inside the intro")
#         print(self)
#         print("Inside the intro")


# a = Animal("Coco")
# a.intro()
# print("Called outside the class")
# print(a)
# print("Called outside the class")

# __init__
# __str__
# __repr__
"""
Converting celsius in farenheite and farenheite in celsius
"""


class Converter:
    def __init__(self):
        pass

    def c_to_f(self):  # bhaneko kunai pani object lai represent ya chinna ko lagi ho
        celsius = int(input("Enter the temperature in celsisus"))
        fahrenheite = (celsius * 9 / 5) + 32
        print(f"The temperatur in farenheite is {fahrenheite}°F")

    def f_to_c(self):
        fahrenheite = int(input("Enter the temperature in farenheite"))
        celsius = (fahrenheite - 32) * 5 / 9
        print(f"The temperatur in celsius is {celsius}°C")


temp = Converter()  # Converter() yo bhaneko class ko object banako
temp.c_to_f()  # yo bhaneko tyo class ko method run gareko ho
temp.f_to_c()  # yo bhaneko tyo class ko method run gareko ho
