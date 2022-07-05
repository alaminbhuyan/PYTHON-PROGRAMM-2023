import itertools


# for i in itertools.count(5,2):
#     if i == 35:
#         break
#     else:
#         print(i, end=" ")

count = 0

# for i in itertools.cycle('AB'):
#     if count > 7:
#         break
#     else:
#         print(i, end=" ")
#         count += 1

# lis = ['geeks', 'for', 'geeks']
#
# iterators = itertools.cycle(lis)
#
# for i in range(6):
#     print(next(iterators), end=" ")

# print(list(itertools.repeat(25, 4)))

print("The cartesian product using repeat:")
print(list(itertools.product([1, 2], repeat=3)))
print()

print("The cartesian product of the containers:")
print(list(itertools.product(['geeks', 'for', 'geeks'], '2')))
print()

print("The cartesian product of the containers:")
print(list(itertools.product('AB', [3, 4])))

