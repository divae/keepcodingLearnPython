from functools import reduce

list_values = [1,2,-1,15,9]

def double(x):
    return x*2

list_double_values = map(double,list_values)
list_double_values1 = map(lambda x: x * 2 ,list_values)

def is_pair(x):
    return x % 2 == 0

list_pairs_values = filter(is_pair, list_values)
list_pairs_values = filter(lambda x: x % 2 == 0, list_values)

unique_value = reduce(lambda collector, next_value : collector + next_value, list_values)
sum100 = reduce(lambda collector,next_value: collector + next_value,range(101))
sum100 = reduce(lambda collector,next_value: collector + next_value,range(101))


print(list(list_double_values))
print(list(list_pairs_values))
print(unique_value)