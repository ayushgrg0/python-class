try:
    num = int(input("Enter a number"))
    result = 10 / num
    print(f'The result is {result}')
except Exception as e:
    print(f"yesto error aayo: {e.__class__.__name__} : {e}")
finally:
    print("Thankyou for using my application!!!")
