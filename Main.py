# No main será possível acessar as funções através do teclado

class Menu: 
    def menu():
        print ("1: Verificar triângulo")
        print ("2: Calcular equação do segundo grau")
        print ("3: Conferir data")
        print ("4: Verificar tamanho do texto")
        print ("5: Analisar CPF")
        print ("6: Contar caracteres")
        print ("7: Sair")

   

    while True:
        escolher = input ("Selecione um dos números: ")
        if escolher in ('1', '2', '3', '4', '5', '6', '7'):
            confirma = float(input("Coloque o número: "))
            if escolher == '1': 
                print("teste")
        else: 
            print ("Adeus")
      
