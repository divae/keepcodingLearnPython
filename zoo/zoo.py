import input_screen
import calculate

YEARS = []

def add_age(position):
    YEARS.append(input_screen.ask_age(position))

def get_position(number):
    return number + 1

def add_people():
    position_y = 3
    persons_number = input_screen.ask_persons_number(position_y)

    for number in range(persons_number):
        position = get_position(number)
        add_age(position)

def sort_years():
    YEARS.sort()
   
def check_in(YEARS):
    return calculate.total(YEARS)
    
  

            
#---------------------------------------------------------------------------------------------------------
def main():
    add_people()        
    payments = check_in(YEARS)
    print(payments)
   # print_average(payments)    
    
main()