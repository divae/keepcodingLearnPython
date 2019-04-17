def normal(value):
    return value

def square(value):
    return value*value

def cube(value):
    return value**3

def amount_all(limit_to,function):

    result = 0
    limit = limit_to+1

    for number in range(0, limit):
        result += function(number)

    return result


if __name__ == '__name__':
    print(amount_all(3,normal))
    print(amount_all(3,square))
    print(amount_all(3,cube))

