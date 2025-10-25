#List comprehension

#1. Take a number from the user, create a list with all the odd numbers under the input value And another list of odd numbers.
#2.Create a list of fruits. Then, convert the first letter of every element to capital and create a new list of updated values.
#3. Make it Simple.

FruitList = ['apple', 'banana', 'mango', 'orange', 'kiwi']
Caps = [fruit.capitalize() for fruit in FruitList]
print(Caps)