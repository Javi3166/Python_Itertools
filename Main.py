# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators
# A module that contains advanced iterators. Iterators are a data type that can be used in for loops

from itertools import product
from itertools import permutations
from itertools import combinations, combinations_with_replacement
from itertools import accumulate
from itertools import groupby
import operator
from itertools import count, cycle, repeat

print("\nProduct finds the cartesian product of two lists. Must convert the result to a list in order to display it.")
a = [1,2]
b = [3,4]
result = list(product(a,b))
print(result)

print("\nIt is also possible to have it repeat multiple times.")
b = [3]
result = list(product(a,b, repeat = 2))
print(result)

print("\nPermutations is used to get a list of all the permutations of a list. It is also possible to limit it to a "
      "certain amount per permutation.")
a = [1, 2, 3]
perm = list(permutations(a))
print(perm)
perm = list(permutations(a, 2))
print(perm)

print("\nCombinations is used to get a list of all combinations of a list. It is required to put how many elements per "
      "result. \nUsing combinations with replacements will allow a number to be duplicated, i.e. [1,1] will be made with "
      "one instance of 1.")
a = [1, 2, 3, 4]
comb = list(combinations(a, 3))
print(comb)
comb = list(combinations_with_replacement(a, 2))
print(comb)

print("\nAccumulate can be used to generate a list of accumulative sums. Can be used with the operator module "
      "to use multiplication \ninstead or show consistently the max value that was processed.")
a = [1,2,5,3,4]
acc = list(accumulate(a))
print("Original list: ", a)
print("With default accumulation(addition): ", acc)
acc = list(accumulate(a, func=operator.mul))
print("Changed to operator to multiplication: ", acc)
acc = list(accumulate(a, func=max))
print("Changed it to show max: ", acc)

print("\nGroupby return an iterable list of keys from another iterable group grouped in a defined way.")
def smaller_than_3(x):
    return x <= 3
a = [1, 2, 3, 4, 5]
group_obj = groupby(a, key=smaller_than_3)
for key, value in group_obj:
    print(key, list(value))

persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}, {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]
group_obj = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj:
    print(key, list(value))

print("\nThere are a few infinite iterators available. Basically functions that will loop through a for loop forever unless "
      "there is a break condition.")
print("\nCount() counts up from whatever the starting value was.")
for index in count(10):
    print(index)
    if index == 50:
        break

print("\nCycle() will cycle through an iterable list forever unless there is a stop condition.")
a = [1, 2, 3]
loop = 0
for index in cycle(a):
    print(index)
    loop += 1
    if loop == 9:
        break

print("\nRepeat() will repeat a selected element forever, but a 2nd argument can be inputted as a stop condition of how "
      "many times it will be repeated.")
for index in repeat(1, 5):
    print(index)