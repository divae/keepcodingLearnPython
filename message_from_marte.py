CODE_HEXADECIMAL = ('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F')
def descompose_message(message):
    return tuple(message)

def convert_str_to_ascii(letter):
    return ord(letter)

def convert_ascii_to_hexadecimal(ascii_number):
    return hex(ascii_number)[2:]

def get_angle():
    TOTAL_CIRCLE = 360
    NUMBER_ANGLES = len(CODE_HEXADECIMAL)
    return TOTAL_CIRCLE / NUMBER_ANGLES

def get_position_in_HEXADECIMAL(value):
    STRvalue = str(value).upper()
    return CODE_HEXADECIMAL.index(STRvalue)

def get_position(__tupla__,position_element):
    value = __tupla__[position_element]
    position = get_position_in_HEXADECIMAL(value)
    return position

def angle_to_send(position,angle):
    return position * angle

def code_message_to_angles(message):    
    message_descompose = descompose_message(message)
    angle = get_angle()
    message_to_send = []

    for letter in message_descompose:
        ascii_number = convert_str_to_ascii(letter)
        
        hexadecimal_code = convert_ascii_to_hexadecimal(ascii_number)
        
        position_one = get_position(hexadecimal_code,0)
        message_to_send.append(angle_to_send(position_one,angle))
        
        position_two = get_position(hexadecimal_code,1)
        message_to_send.append(angle_to_send(position_two,angle))
        
    return message_to_send
        
def send_message(message):
    print(message)
#----------------------------------------------------------        
message = "hello world"
message_codified = code_message_to_angles(message)
send_message(message_codified)

    