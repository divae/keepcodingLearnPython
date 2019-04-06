def sum_first_100_numbers_for():
    total = 0
    for incremental_value in range(1, 101):
        total += incremental_value
        
    return total

def sum_first_100_numbers_while():
    total = 0
    incremental_value = 1
    
    while incremental_value < 101:
        total += incremental_value
        incremental_value += 1
        
    return total


value_for = sum_first_100_numbers_for()
value_while = sum_first_100_numbers_while()

print("The value of the sum of the first numbers are: ", value_for)
print("The value of the sum of the first numbers are: ", value_for)
