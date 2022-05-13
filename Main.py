# No main será possível acessar as funções através do teclado
from Triangulo import TiposDeTriangulo



class Menu: 
    def menu():
        print ("1: Verificar triângulo")
        print ("2: Calcular equação do segundo grau")
        print ("3: Conferir data")
        print ("4: Verificar tamanho do texto")
        print ("5: Analisar CPF")
        print ("6: Contar caracteres")
        print ("7: Sair")

    def op1 ():
            return TiposDeTriangulo

    while True:
        escolher = float (input ("Selecione um dos números: "))
        if escolher in ('1', '2', '3', '4', '5', '6', '7'):
            num1 = float(input(op1))

            if escolher == "1":
                print(num1, op1)

        else: break
