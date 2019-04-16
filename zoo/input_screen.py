import validate_numbers

def question(position_y,STRquestion):
    STRnumber = input(STRquestion)
    number = validate_numbers.format_to_integer(STRnumber)
    return number if number != None else question(STRquestion)

def ask_persons_number(position_y):
    STRquestion = 'How many people there are in a group?: '
    position_y = 3
    return question(position_y,STRquestion)

def ask_age(position_y):
    STRquestion = f"What age have the {position_y} member?: "
    return question(position_y,STRquestion)

def print_average(payments):
    print(payments)

    print('--Products--')

    for payment_type in payments:
        print(f"{payment_type['count']} entrada de baby ({payment_type['price']}€)   total:  {payment_type['total']}")
    
    print('--Total--')
    print(f'{total_price}€')