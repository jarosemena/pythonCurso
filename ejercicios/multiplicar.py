def multiplicar( a, b, resp = 0  ):   
    if b == 0:
       None
    else:
        #resp = resp + a
        resp = multiplicar (a, b-1,resp) + a
    return resp
   
print('la respuesta es= ', multiplicar( 4,8))