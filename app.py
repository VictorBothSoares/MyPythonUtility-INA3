import sys
from calculadora import *

#Seleciona função
#1 - Calculadora
#2 - Inverte string
#3 - Ordena caracters da string
#4 - Retorna dia da semana para data
#5 - Detecta palíndromos
#6 - Retorna se é número é par ou impar
#7 - Sorteia um número aleatório para um dado intervalo numérico
#8 - Verifica se palavra/caracter existe na string
#9 - Imprime o número Pi com x casas decimais 
#Enter - Sair
print("informe a funcão:\n1 - Inverte string\n2 - Inverte string - Calculadora\n9 - Pi com x casas decimais" +
      "\nEnter - Sair")
funcao = input()
if (funcao == "1"):
    calculate()
elif (funcao == "2"):
    string = input("Digite a string a ser invertida: ")
    print(string[::-1])
elif (funcao == '9'):
    pi()
else:
    print("Função não implementada!") 
print("Bye!")
