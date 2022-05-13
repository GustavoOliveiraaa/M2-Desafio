# Irá verificar um triângulo nessa classe

#Utilizei Def, de acordo com a documentação do python, esse comando serve para definir funções que terão uma sequencia de comandos.
# And: Retorna True se ambas as declarações forem True
class TiposDeTriangulo:
#Definir se o triangulo está ok
    def tudo_certo (a,b,c):
        if a+b>=c and b+c>=a and c+a>=b:
            return True
        
        else: 
            return False

    def tipo_do_triangulo (a,b,c):
        if a==b or b==c or a==c:
            print("O triângulo é: Isósceles ")
        elif a==b and b==c:
            print("O triângulo é: Equilátero")
        else:
            print ("O triângulo é: Escaleno")

    # Essa parte ele irá ler os devidos lados
    lado_a = float (input("Digite o comprimento do lado A: "))
    lado_b = float (input("Digite o comprimento do lado B: "))
    lado_c = float (input("Digite o comprimento do lado C: "))

    # Método que mostre o resultado dos triângulos:

    if tudo_certo (lado_a, lado_b, lado_c):
        tipo_do_triangulo (lado_a, lado_b, lado_c)

    else:
        print ("Não é possivel determinar o triângulo, tente outros valores.")