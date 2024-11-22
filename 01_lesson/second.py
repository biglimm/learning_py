from collections import OrderedDict

my_dict = {'b': 2, 'a': 1, 'c': 3}
sorted_dict = OrderedDict(sorted(my_dict.items()))

print(type(sorted_dict))
print(sorted_dict)