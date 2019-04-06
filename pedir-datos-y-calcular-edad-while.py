mes01 = 31
mes02 = 28
mes03 = 31
mes04 = 30
mes05 = 31
mes06 = 30
mes07 = 31
mes08 = 31
mes09 = 30
mes10 = 31
mes11 = 30


meses = (mes01,mes02,mes03,mes04,mes05,mes05,mes06,mes07,mes08,mes09,mes10,mes11)

nombre = input("¿Como te llamas?")
print("Hola, ",nombre)

strEdad = input("¿Cuantos años tienes?")
strAnno = input("¿En que año estamos?")
strMes = input("En que mes estamos")
strDia = input("¿En qué día estamos")


edad = int(strEdad)
anno = int(strAnno)
mes = int(strMes)
dia = int(strDia)

transcurridos = 0
indice = 0

while indice < mes -1:
    transcurridos = transcurridos + dia
    indice = indice + 1
    
prob = transcurridos / 365 * 100
nacimiento = anno - edad

print(nombre, "nacieste en", nacimiento, "con una probabilidad de", prob)
print(" o en ", nacimiento - 1, "con una probabilidad de", 100- prob)
 