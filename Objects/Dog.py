
class Dog():
    def __init__(self,name,year,weight):
        self.__name = name
        self.__year = year
        self.__weight = weight

    def bark(self):
        print("Guau Guau")

    def name(self):
        return self.__name
    
    def year(self):
        return self.__year

    def weight(self):
        return self.__weight

    def __str__(self):
        return "I'm {}, year:{}, weight:{}".format(self.__name,self.__year,self.__weight)

class AssistantDog(Dog):
    def __init__(self, name, year, weight, owner):
        Dog.__init__(self, name, year, weight)
        self.__owner = owner
        self.working = False

    def bark(self):
        if self.working:
            print("Shhh, I can't bark")
        else:
            Dog.bark(self)
    
    def __str__(self):
        return "Dog {}, year:{}, weight:{},Assistan of owner:{}".format(self.name(),self.year(),self.weight(),self.__owner)






dog = Dog('Sora',2,10)

dog.bark()
print(dog)

assistandog = AssistantDog('Sora',2,10,'Estela')

assistandog.bark()
assistandog.working = True
assistandog.bark()

print(assistandog)