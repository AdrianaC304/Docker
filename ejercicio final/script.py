#import sys
#print (len (sys.argv))
#print (sys.argv)


import sys

def suma(a, b):
    return a + b
    
numero1 = float(sys.argv[1])
numero2 = float(sys.argv[2])
resultado = suma(numero1, numero2)
print(f"La suma de {numero1} y {numero2} es: {resultado}")
