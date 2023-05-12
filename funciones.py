#FUBNCIONES

#CONVERSOR DE FAHRENHEIT A KELVINS 

def conversor(numero,temperatura):
    if temperatura == 'K' or temperatura =='k':
        x= (numero - 32) * 5/9 + 273.15 
    elif temperatura == 'F' or temperatura =='f':
        x = (numero - 273.15) * 9/5 + 32 
    else:
        print('seleccione una temperatura sea K o F')
    return (x)
resultado= conversor (20,'f')
print('tu resultado es: {}'.format(resultado))


#Ejercicio de suma de elementos:

def suma(x,y,a):
    c=(x+y+a)
    return (c)

result=suma(10,20,10)
print (result)


