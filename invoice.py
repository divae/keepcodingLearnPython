PRICE = 0
UNIT = 1

DECIMALS_NUMBER = 2

TOTAL_PRICE = 0
TOTAL_UNITS = 0

CMD_ERROR = "\033[1;31;37m"
CMD_NORMAL = "\033[0;37;40m"

def print_error():
    print(CMD_ERROR)
    print("--------------------Error, vuelva a intentarlo-----------------")
    print(CMD_NORMAL)
        
def format_to_float(value):
    try:
        number = round(float(value),DECIMALS_NUMBER)    
    except:
        print_error()
        number = None
        
    return number

def formar_to_integer(value):
    try:
        number = int(value)    
    except:
        print_error()
        number = None        
    return number

def is_number(value):
    return False if formar_to_integer(value) != None else True

def salute():
    print("Bienveido a nuestra tienda:")

def ask_number_new_products():
    number = formar_to_integer(input("¿Con cuantas unidades de productos diferentes empiezas el día? \n"))
    return number if number != None else ask_number_new_products()

def ask_head_new_product():
    print("------------------Add product--------------")
    
def new_price_product():
    price = format_to_float(input("¿Precio unitario del producto? : "))
    return price if price != None else new_price_product()

def new_count_product():
    count = formar_to_integer(input("¿Unidades del producto? : "))
    return count if count != None else new_count_product()

def new_product():
    ask_head_new_product()
    
    price = new_price_product()
    count = new_count_product()
    
    return [price,count] if (price != None and count != None )else new_product() 

def new_stock(total_new_products):
    list_products = []
    for value in range(0, total_new_products):
        list_products.append(new_product())
    
    return list_products

def show_resume(list):
    TOTAL_PRICE = 0
    TOTAL_UNITS = 0
    print("------------------ Resumen --------------------")
    for product in list:
        price_product = product[PRICE]
        unit_product = product[UNIT]
        
        total_price_same_product = round(price_product * unit_product,DECIMALS_NUMBER)
        
        print(price_product,"€ - ", unit_product, " units - ", total_price_same_product,"€")
        
        TOTAL_PRICE += total_price_same_product
        TOTAL_UNITS += unit_product
    print("--------------------------------------")  
    print("Total €: ",TOTAL_PRICE)
    print("Total units", TOTAL_UNITS)
        

salute()

total_units = ask_number_new_products()

stock = new_stock(total_units)

show_resume(stock)



   