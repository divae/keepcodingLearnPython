def contain(list,index):
    try:
        result = list[index]
    except:
        result = None
        
    return result    
    
def sumTotalNotes(list):
    total = 0
    for value in list:
        if(contain(list,value) != None ): 
            total += value
        
    return total
       
def numberNotes(list):
    return len(list)

def calculate_around(list):
    numberItems = numberNotes(list)
    totalNotes = sumTotalNotes(list)
    return round(totalNotes / numberItems, 2)

def printResult(total):
    print("The total are: ",total)
        
listNotes = (1,2,3,4)
around = calculate_around(listNotes)
    
printResult(around)