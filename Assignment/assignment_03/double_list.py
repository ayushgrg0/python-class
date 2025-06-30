'''
Question 8. Double List Elements
Write a function double_list that takes a list of numbers and returns a new list where each element is doubled.
Use a loop instead of map().
Example:

Input: double_list([1, 2, 3])
Output: [2, 4, 6]
Input: double_list([5, 10])
Output: [10, 20]
'''


def double_list(value):
    new_lst = []
    for ele in value:
        double_value = ele + ele
        new_lst.append(double_value)
    print(new_lst)


double_list([1, 2, 3])
double_list([5, 10])
