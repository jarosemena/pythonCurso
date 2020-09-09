contador = 0 

while contador < 10 :   
    print(contador)
    contador +=1 
 

contadorExterno = 0 
contadorInterno = 0 

while contadorExterno < 5 :
    while contadorInterno < 6 :
        print(contadorExterno, contadorInterno)
        contadorInterno += 1

        if contadorInterno >=3:
            break

    contadorExterno += 1 
    contadorInterno = 0     