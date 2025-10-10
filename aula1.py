resultado = 8 // 3 #resto da divisão 
print(resultado)
print(type(4.5))
print(type("4.5"))
print(type(True))
print(8%2)
a, b, c, x = 5, 6, 7, 1
print(x)
teste = 'string pequena' 
print(teste*4)
resultado = teste.split(" ")
print(teste.count("n"))
print(resultado[0] == resultado[1])
nomes = [23, 45.4,"Clesio", "Justino", "Geugres, Maciel" ]
nomes[0] = "ELisângela" 
del nomes[5]
print(nomes)
print(23 in nomes)
print(max(nomes))
a = [1, 2, 3, 4] #lista
b = (1, 2, 3, 4) #tupla
c = {1, 2, 3, 4} #dicionario
idade = 17
if idade > 18: #idade <= 18
        print("Adulto")
elif idade > 16:
        print("Adolescente")
else: 
        print("criança")
# a logica é que teu segundo if ja passou pelo primeiro 
# or, not, or not ESTUDAR SOBRE ISSO!
lista1 = [i for i in range(0,10)] #list_comprenshions
lista2 = [0, 1,2, 3, 4, 5, 6, 7, 8, 9] #mesma coisa da lista1, pq?!
for i in range(0, 10):
        print(i+1)
for i in lista1:
        for j in lista2:
                print(i,j)
for i in range(10, 0, -1):
        print(i)
valor = 0
while valor < 10:
    print("loop infinito")
    valor+=1 
def pitagoras(cateto_a, cateto_b);
        hipotenusa = cateto_a ** 2 + cateto_b ** 2
        return hipotenusa ** 2
print(pitagoras(2, 3))
def potencia(num):
        return num ** 2
print(potencia(5))
import numpy as np
print(np.sqrt(9))
#enumerete e elemento
#try, except, zerodivisionerror
#init, pass, self