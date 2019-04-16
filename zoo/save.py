from config import preciosE 

FILE = open("transaction.txt",'w+')
number_ticket_baby = 0
number_ticket_young = 0
number_ticket_normal = 0
number_ticket_senior = 0

    
transaction = "3,0,2,1\n"
transaction += "2,1,4,1\n"

FILE.write(transaction)
FILE.close()


FILE = open("transaction.txt",'r')

register = FILE.readline()

while register != '':
    ticket = register.split(',')
    
    number_ticket_baby += int(ticket[0])
    number_ticket_young += int(ticket[1])
    number_ticket_normal += int(ticket[2])
    number_ticket_senior += int(ticket[3])
    
    register = FILE.readline()

print("Entradas de Bebe.......:{:3d} - {:7.2f}".format(number_ticket_baby,number_ticket_baby * preciosE["baby"] ))
print("Entradas de Niño.......:{:3d} - {:7.2f}".format(number_ticket_young,number_ticket_young * preciosE["young"]))
print("Entradas de Aduto......:{:3d} - {:7.2f}".format(number_ticket_normal,number_ticket_normal * preciosE["normal"]))
print("Entradas de Jubilado...:{:3d} - {:7.2f}".format(number_ticket_senior,number_ticket_senior * preciosE["senior"]))
