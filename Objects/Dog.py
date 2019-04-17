
class Dog():
    def __init__(self,name,year,weight):
        self.name = name
        self.year = year
        self.weight = weight

    def bark(self):
        print("Guau Guau")
    
    def __str__(self):
        return "I'm {}, year:{}, weight:{}".format(self.name,self.year,self.weight)


dog = Dog('Sora',2,10)

dog.bark()
print(dog)