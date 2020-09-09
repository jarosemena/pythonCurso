import sys

def divide_elemtosLista(lista, divisor ):
    try:
        return [i /divisor for i in lista]
    except ZeroDivisionError as ex:
        return lista
 #   except Exception as e: 
 #       return lista 
    except: # catch *all* exceptions
      e = sys.exc_info()[0]
      
      print( f'Error type:   {e}' )
      return lista
      
lista = list(range(10))

divisor = 0

print (divide_elemtosLista(lista, divisor ))
