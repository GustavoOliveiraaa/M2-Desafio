from pickle import TRUE  

triangulo = 1
equacao = 2
data = 3
texto = 4
cpf = 5
caracteres = 6
sair = 7

print("Olá Fulano.")
print("Opções: ")
print("1) Verificar triângulo  ")
print("2) Calcular equação do segundo grau  ")
print("3) Conferir data  ")
print("4) Verificar tamanho do texto  ")
print("5) Analisar CPF  ")
print("6) Contar caracteres  ")
print("7) Sair  ")

menu = int(input("Digite a opção desejada: "))
while True:
  if menu == 1:
       if triangulo: 
                  def tudo_certo (a,b,c):
                      if a+b>=c and b+c>=a and c+a>=b:
                          return True
                      else: 
                          return False
                  def tipo_do_triangulo (a,b,c):
                     if a==b and b==c:
                         print("O lado do triângulo é Equilátero.")

                     elif a==b or b==c or a==c:
                        print("O lado do triângulo é Isósceles.")    

                     else:
                      print("O lado do triângulo é Escaleno.")
                          
                  lado_a = float (input("Digite o comprimento do lado A: "))
                  lado_b = float (input("Digite o comprimento do lado B: "))
                  lado_c = float (input("Digite o comprimento do lado C: "))
  
                  if tudo_certo (lado_a, lado_b, lado_c):
                      tipo_do_triangulo (lado_a, lado_b, lado_c)                          
                  else:
                      print ("Não é possivel determinar o triângulo, tente outros valores.")
                           
  elif menu == 2:
    if menu: 
        print("Equação do segundo grau: ax^2 + bx + c = 0")

        a = float(input("Digite o valor da variável 'A' da equação: "))
        b = float(input("Digite o valor da variável 'B' da equação: "))
        c = float(input("Digite o valor da variável 'C' da equação: "))
        delta = (b**2) - 4*a*c

        if a == 0:
            print("O valor de A não pode ser zero: Isso não é uma equação de segundo grau!") 
        elif delta < 0:
            print("A equação não possui raízes reais, lembre-se que o delta não pode ser negativo! ")
        elif delta == 0:
            unicaRaiz = (-b + delta ** (1 / 2)) / (2 * a)
            print("X1: {}".format(unicaRaiz))

        else: 
            resposta1 = (-b + delta ** (1 / 2)) / (2 * a)
            resposta2 = (-b - delta ** (1 / 2)) / (2 * a)
            print("X1: {}, X2: {} ".format(resposta1,resposta2))
       

  elif menu == 3:
                data = input("Insira uma data (dia/mês/ano): ")
                dia,mes,ano=data.split('/')
                dia = int(dia)
                mes = int(mes)
                ano = int(ano)
                
                if (mes==1 or mes==3 or mes== 5 or mes==8 or mes== 10 or mes==12):
                    ultimoDiadoMes = 31
                elif (mes==4 or mes==6 or mes==9 or mes==11):
                    ultimoDiadoMes = 30
                elif (mes==2):
                    ultimoDiadoMes = 28
                else:
                   print("Tente um mês válido!")
                if(mes<1 or mes>12):
                    print("Data inválida")
                elif(dia<1 or dia>ultimoDiadoMes):
                    print("Data inválida")
                elif(dia==ultimoDiadoMes and mes!=12):
                    dia=1
                    mes=mes+1
                    print("Data válida: ")
                elif(dia==31 and mes==12):
                     dia=1
                     mes=1
                     ano=ano
                     print("Data válida ")
                else:
                    dia=dia
                    print("Data válida:")

  elif menu == 4:
    texto = input("Coloque seu texto: ")
    x = len(texto)
    if x < 5:
        print("Texto muito pequeno")
    elif x == 5 or x == 6 or x == 7 or x == 8 or x == 9 or x == 10 or x == 11 or x == 12 or x == 13 or x == 14:
        print("Texto médio")    
    elif x==15 or x==16 or x== 17 or x== 18 or x== 19 or x== 20:
        print("Texto grande")
    else:
        x > 20
        print("Texto inválido")
    
  elif menu == 5:
      inserirCpf = input("Coloque seu CPF sem traços e pontos: ") 
      y =  len (inserirCpf)
      if y == 11:
        print("CPF Válido")
      elif y== 1 or y== 2 or y== 3 or y== 4 or y== 5 or y== 6 or y== 7 or y== 8 or y== 9 or y== 10 or y > 11:
          print("CPF Inválido")
      else:
          y > 11
          print("CPF Inválido")

  elif menu == 6:
    textoDoContador = input("Coloque seu texto: ")
    vogal = 0
    consoante = 0
    
    for caracter in textoDoContador:
        if caracter in ("a","i","u","e","o","A","I","U","E","O","á","à","ã","â","í","ú","é","ê","í"):
            vogal = vogal + 1
        
        else:
            consoante = consoante + 1
            
    print("Vogais: %d" %vogal)
    print("Número de Consoantes: %d " %consoante)
  
  elif menu == 7:
    print("Obrigado por utilizar nosso sistema")
    break

  else:
     menu > 7
     print("Erro!")
     break