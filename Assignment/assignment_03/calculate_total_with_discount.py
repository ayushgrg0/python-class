'''
Question 15. Calculate Total with Discount
Write a function calculate_total that takes any number of item prices
and an optional discount percentage (default to 0). Return the total cost after applying the discount.
Example:

Input: calculate_total(10, 20, 30, discount=10)
Output: 54 (60 - 10% of 60 = 54)
Input: calculate_total(100, 200)
Output: 300
'''


def calculate_total(*prices, discount=10):
    total = sum(prices)

    discount_amt = total * (discount / 100)
    final_amt = total - discount_amt
    print(f'The final amount after providing a 10% discount is NPR-{final_amt}')


calculate_total(10, 20, 30, discount=10)
calculate_total(100, 200)
