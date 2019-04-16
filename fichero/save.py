file_purchases = open("transaction.txt",'w+')

transaction = "3,0,2,1\n"
transaction += "2,1,4,1\n"

file_purchases.write(transaction)
file_purchases.close()

