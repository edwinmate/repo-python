print("Hola Mundo")

my_lista=[20,30,80,80]

my_dic={'saludo':'hola','despedida':'chao','animal':'gato'}

for element in my_lista:
    
    if element > 20:
        print(element)
    else:
        print('es diferente a 20')
        break
        

my_tupla=('hola','perro','gato','youtube')

for my_element in my_tupla:
    #print (my_element)
    if not my_element == 'hola':
        print (my_element)

numero=0
while (numero <= 10):
    print(numero)
    numero +=1

nume=0
while (nume <= 12):
    if nume % 2 == 0:
        print(nume,'el numero es par')
    else:
        print(nume,'el numero es impar')
    numero +=1

    break



