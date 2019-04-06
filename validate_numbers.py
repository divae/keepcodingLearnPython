def print_error():
    print("--------------------Error, vuelva a intentarlo con un número -----------------")
    
def format_to_integer(value):
    try:
        number = int(value)    
    except:
        print_error()
        number = None        
    return number

def is_number(value):
    return False if format_to_integer(value) != None else True

def question(STRquestion):
    number = format_to_integer(input(STRquestion))
    return number if number != None else question(STRquestion)

