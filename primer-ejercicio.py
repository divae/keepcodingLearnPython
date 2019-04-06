   
try:
    while True:
        strPrimerNumero = input(" dame un número ")
        strSegundoNumero = input(" dame otro número ")
       
        primerNumero = int(strPrimerNumero)
        segundoNumero = int(strSegundoNumero)
        
        primerNumero = primerNumero/10
        segundoNumero = segundoNumero/10
        
        
        if(isinstance(strPrimerNumero, int) and isinstance(strSegundoNumero, int) ):
            break

        suma = round(primerNumero + segundoNumero,2)
        resta = round(primerNumero - segundoNumero,2)
        multiplicacion = round(primerNumero * segundoNumero,2)
        division = round(primerNumero / segundoNumero,2)

        print("El resultado de la suma es: ", suma)
        print("El resultado de la resta es: ", resta)
        print("El resultado de la multiplicación es: ", multiplicacion)
        print("El resultado de la división es: ", division)

except ValueError:
    sum_first_100_first_numbersprint("Favor ingrese un numero entero")
pass
