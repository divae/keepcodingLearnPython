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
    return format_to_integer(value) != None


