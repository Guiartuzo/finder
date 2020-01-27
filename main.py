import sqlquerry

id1 = input("o que deseja? ")
#print(id1)

id2 = input("Digita a {} que deseja " .format(id1))

sqlquerry.getMaterial(id1,id2)
