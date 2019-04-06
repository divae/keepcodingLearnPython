import validate_numbers

YEARS = []
PAYMENT = {}

PRICES = {
    "baby" : 0.00,
    "young" : 42.00,
    "normal" : 46.00,
    "senior" : 18.00,
    }

def count_in_range(__list__, initial, final): 
    count = 0 
    for value in __list__:
        if value>=initial and value<=final: 
            count+= 1
    return count

def ask_persons_number():
    question = 'How many people there are in a group?: '
    return validate_numbers.question(question)

def ask_age(position):
    question = f"What age have the {position} member?: "
    return validate_numbers.question(question)

def get_position(number):
    return number + 1

def add_age(position):
    YEARS.append(ask_age(position))

def add_people():
    persons_number = ask_persons_number()

    for number in range(persons_number):
        position = get_position(number)
        add_age(position)

def sort_years():
    YEARS.sort()
    
def count_babies():
    return YEARS.count(0)

def count_young():
    return count_in_range(YEARS,1,17)

def count_normal():
    return count_in_range(YEARS,18,64)

def count_senior():
    return count_in_range(YEARS,65,200)

def recount_babies():
    PAYMENT["baby"] = count_babies()
    
def recount_youngs():
    PAYMENT["young"] = count_young()

def recount_normals():
    PAYMENT["normal"] = count_normal()

def recount_seniors():
    PAYMENT["senior"] = count_senior()
    
def total_price_baby():
    return PAYMENT['baby'] * PRICES['baby']

def total_price_young():
    return PAYMENT['young'] * PRICES['young']

def total_price_normal():
    return PAYMENT['normal'] * PRICES['normal']

def total_price_senior():
    return PAYMENT['senior'] * PRICES['senior']

def total_price():
    return total_price_baby() + total_price_young() + total_price_normal() + total_price_senior()
    
def check_in():
    recount_babies()
    recount_youngs()
    recount_normals()
    recount_seniors()
  
def print_average():
    print('--Products--')
    
    print(f"{PAYMENT['baby']} entrada de baby ({PRICES['baby']}€)   total:  {total_price_baby()}")
    
    print(f"{PAYMENT['young']} entrada de young ({PRICES['young']}€)   total:  {total_price_young()}")
    
    print(f"{PAYMENT['normal']} entrada de normal ({PRICES['normal']}€)   total:  {total_price_normal()}")
    
    print(f"{PAYMENT['senior']} entrada de senior ({PRICES['senior']}€)   total:  {total_price_senior()}")
    
    print('--Total--')
    print(f'{total_price()}€')
            
#---------------------------------------------------------------------------------------------------------

add_people()
    
check_in()   
print_average()    
    
