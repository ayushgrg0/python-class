'''
Question 1. **FizzBuzz with a Twist (Loops and Conditionals)**
Write a program that prints numbers from 1 to 50. For multiples of 3, print "Fizz"; for multiples of 5,
print "Buzz"; for multiples of both, print "FizzBuzz". Additionally, if the number is even, append "Even" to the output
(e.g., 15 should print "FizzBuzzEven"). Use loops and conditionals to implement this.
'''

number = range(1, 50)

for num in number:
    if num % 3 == 0 and num % 5 == 0:
        print(f"{num} --- FizzBuzz")
    elif num % 3 == 0:
        print(f"{num} --- Fizz")
    elif num % 5 == 0:
        print(f"{num} --- Buzz")
    elif num % 2 == 0:
        print(f"{num} --- FizzBuzzEven")
