import sys

def formar_to_float(value):
    try:
        number = float(value)    
    except:
        number = None
        
    return number    

def calculate_area_triangle(height,width):
    area = (height * width)/2
    return area

def area_triangle(height,width):
    
    height = formar_to_float(height)    
    width = formar_to_float(width)
    
    if(height == None or width == None):
        return "Error"
    
    area = calculate_area_triangle(height,width)
    
    rounded_area = round(area,2)
    
    return rounded_area

def print_area(area):
    print(".................................")
    print("The area of a triangle is", area)
    print(".................................")
    
if __name__ == '__main__':
    number_arguments = 3
    if len(sys.argv) >= number_arguments:
        position_height = 1
        position_width = 2
        S_height = float(sys.argv[position_height])
        S_width = float(sys.argv[position_width])
    else:
        S_height = input("give me a height: ")
        S_width = input("dive me a width: ")
     
    area = area_triangle(S_height,S_width)

    print_area(area)


