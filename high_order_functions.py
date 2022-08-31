from functools import reduce

my_list = [1,2,3,4,5,6]
pairs = list(filter(lambda x: x%2==0, my_list))
square = list(map(lambda x: x**2, my_list))
colapse = reduce(lambda x,y:x+y, my_list)
print(square)
print(colapse)