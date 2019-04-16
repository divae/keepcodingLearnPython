import prices

PAYMENT = {}
YEARS = []

def count_in_range(__list__, initial, final): 
    count = 0 
    for value in __list__:
        if value>=initial and value<=final: 
            count+= 1
    return count

def count_babies():
    return YEARS.count(0)

def count_young():
    return count_in_range(YEARS,1,17)

def count_normal():
    return count_in_range(YEARS,18,64)

def count_senior():
    return count_in_range(YEARS,65,200)

def recount_babies():
    PAYMENT["baby"] = {"count" : count_babies()}
    
def recount_youngs():
    PAYMENT["young"] = {"count" : count_young()}

def recount_normals():
    PAYMENT["normal"] = {"count" : count_normal()}

def recount_seniors():
    PAYMENT["senior"] = {"count" : count_senior()}

def price_babies():
    PAYMENT["baby"]["price"] = prices("baby")
    
def price_youngs():
    PAYMENT["young"]["price"] = prices("young")

def price_normals():
    PAYMENT["normal"]["price"] = prices("normal")

def price_seniors():
    PAYMENT["senior"]["price"] = prices("senior")
 
def total_price_baby():
    PAYMENT["senior"]["total"] = PAYMENT["baby"] * prices.get["baby"]


def total_price_young():
    PAYMENT["senior"]["total"] = PAYMENT["young"] * prices.get["young"]

def total_price_normal():
    PAYMENT["senior"]["total"] = PAYMENT["normal"] * prices.get["normal"]

def total_price_senior():
    PAYMENT["senior"]["total"] = PAYMENT["senior"] * prices.get["senior"]

def total_price():
    PAYMENT["total"] = total_price_baby() + total_price_young() + total_price_normal() + total_price_senior()
    

def total(years):
    YEARS = years
    recount_babies()
    recount_youngs()
    recount_normals()
    recount_seniors()

    return PAYMENT

