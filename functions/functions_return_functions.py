def is_empty_list(number):
    return number == 0

def error():
    return 0

def maximun(*numerical_list):
    
    maximun_value = numerical_list[0]
    
    initial_value = 1
    total_quantity = len(numerical_list)

    if is_empty_list(total_quantity):
        return error()

    for number in range(initial_value, total_quantity):

        actual_value = numerical_list[number]

        if actual_value > maximun_value:
            maximun_value = actual_value

    return maximun_value
    
def minimun(*numerical_list):
    
    minimun_value = numerical_list[0]
    
    initial_value = 1
    total_quantity = len(numerical_list)

    if is_empty_list(total_quantity):
        return error()

    for number in range(initial_value, total_quantity):

        actual_value = numerical_list[number]

        if actual_value < minimun_value:
            minimun_value = actual_value

    return minimun_value

def average(*numerical_list):
    
    minimun_value = numerical_list[0]
    
    total_quantity = len(numerical_list)

    if is_empty_list(total_quantity):
        return error()

    total = 0

    for number in numerical_list:
        total += number

    return total / total_quantity

function_manager = {
    'maximun' : maximun,
    'minimun' : minimun,
    'average' : average
}

def run_function(name):
    name = name.lower() 
    if name in function_manager.keys():
        return function_manager[name]

if __name__ == '__name__':
    print(run_function('maximun')(1,3,-1,15,9))
    print(run_function('minimun')(1,3,-1,15,9))
    print(run_function('average')(1,3,-1,15,9))