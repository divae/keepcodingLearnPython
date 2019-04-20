
class TemperatureConverter():
   
    def __init__(self,unit,degrees):
        self.__set_units()
        self.__set_unit(unit)
        self.__set_degrees(degrees)

    def show(self):
        print(self.__convert())
        
    def add_unit(self,unit = None):
        is_valid = self.__is_unit_valid(unit)
        set_value = self.__set_unit(unit)
        set_value if is_valid else print("Return to select type of unit")

    def add_degrees(self,degrees = None):
        is_valid = self.__are_degrees_valids(degrees) 
        set_value = self.__set_degrees(degrees)
        set_value if is_valid else print("Return to select type of degrees")

    def __str__(self):
        return "{}º {}".format(self.__degrees, self.__unit)

    def __set_units(self):
        self.__units = {
            "C": self.__celsius_to_farenheit,
            "F": self.__farenheit_to_celsius
            }

    def __is_unit_valid(self,unit):
        try:
            unit = unit.upper()
        except:
            self.__set_unit("Fail in type of unit ")
        
        return unit in self.__units

    def __are_degrees_valids(self,degrees):
        try:
            degrees =  int(degrees)  
        except:
            degrees = None
            self.__set_degrees("Fail in degrees ")
        
        return degrees != None

    def __set_unit(self,unit):
        self.__unit = unit
    
    def __set_degrees(self,degrees):
        self.__degrees = degrees

    def __convert(self):
        return self.__units[self.__unit]
    
    def __celsius_to_farenheit(self):
        return round(self.__degrees * (9/5) + 32,2)

    def __farenheit_to_celsius(self):
        return round((self.__degrees - 32) * (5/9),2)

