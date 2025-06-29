
try:
    num = int(input("Enter a number : "))
    divide = num / 0
    print(divide)
except Exception as e:
    print(f'The error is {e.__class__.__name__}')


'''
Keyboard interrupt
'''

# def print_message(message):
#     print.sleep(10)
