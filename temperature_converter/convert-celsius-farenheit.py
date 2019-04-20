def celsius_to_farenheit(defrees):
    return round(defrees * (9/5) + 32,2)

def farenheit_to_celsius(defrees):
    return round((defrees - 32) * (5/9),2)

def print_to_farenheit(init,fin):
    for defrees in range(init,fin+10,10):
        print("{}ºF -> {}ºC".format(defrees,celsius_to_farenheit(defrees)))

def print_to_celsius(init,fin):
    for defrees in range(init,fin+10,10):
        print("{} ºF -> {} ºC".format(defrees,farenheit_to_celsius(defrees)))
        
def convert(type):
    if type == 'C':
        print_to_celsius(0,230)
    elif type == 'F':
        print_to_farenheit(0,1000)
    else:
        print("Incorrect Type")

def salute():
    print("Hi!")
    
def type():
   type = input("Put 'C' o 'F' to transformation: " )
   return type.upper()

salute()
convert(type())