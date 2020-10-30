import os
os.system('clear') or None

def manipulacao_arquivo(numero):
    nome_arquivo = str(numero) + ".json"
    arquivo = open(nome_arquivo,"r")

    json_string = arquivo.read()

    retirados = ["Exercicios","\n","[","]","\"",":"," ","{","}"]

    clean_string = json_string

    for i in range(0,len(retirados)):
        clean_string = clean_string.replace(retirados[i],"")

    clean_list = clean_string.split(",")

    return clean_list


def print_categoria(categoria):

       if(categoria == 1):
            print("Iniciante")
       elif(categoria == 2):
            print("AD-HOC")
       elif(categoria == 3):
            print("Strings")
       elif(categoria == 4):
            print("Estruturas e Bibliotecas")
       elif(categoria == 5):
            print("Matemática")
       elif(categoria == 6):
            print("Paradigmas")
       elif(categoria == 7):
            print("Grafos")
       elif(categoria == 8):
            print("Geometria Computacional")
       elif(categoria == 9):
            print("SQL")

def ordenacao_dificuldade(lista_completa,quantos):
    
    dificuldades = []
    exercicios = []
    
    for i in range(1,len(lista_completa),2):
        dificuldades.append(lista_completa[i])
    for i in range(0,len(lista_completa),2):
        exercicios.append(lista_completa[i])
    
    for i in range(0,len(exercicios)):
        for j in range(0,len(exercicios)-1):
            if(int(dificuldades[j]) > int(dificuldades[j+1])):
               
                aux = dificuldades[j]
                dificuldades[j] = dificuldades[j+1]
                dificuldades[j+1] = aux

                aux = exercicios[j]
                exercicios[j] = exercicios[j+1]
                exercicios[j+1] = aux

    x = 1
    for i in range(0,len(exercicios)):
        if(int(dificuldades[i]) == int(x)):
            
            print("\n" + "----------" + "Dificuldade " + str(x) + "----------")
            x = x + 1
            
        print(exercicios[i])
    
    print("")
    
    if(quantos != 0):
        for i in range(0,len(exercicios)):
            x=0
            while(x < quantos):
                print(exercicios[i],end=" ")
                x = x + 1
            print("")

def ordenacao_exercicio(dificuldade,lista_completa,quantos):
    
    dificuldades = []
    exercicios = []
    
    for i in range(1,len(lista_completa),2):
        dificuldades.append(lista_completa[i])
    for i in range(0,len(lista_completa),2):
        exercicios.append(lista_completa[i])
    
    if(dificuldade == 1):
        for i in range(0,len(exercicios)):
            print(exercicios[i] + "|" + str(dificuldades[i]))
    elif(dificuldade == 2):
        for i in range(0,len(exercicios)):
            print(exercicios[i])

    



# Filtragem

'''
Categorias
# [1] - Iniciante
# [2] - AD-HOC
# [3] - Strings
# [4] - Estruturas e Bibliotecas
# [5] - Matemática
# [6] - Paradigmas
# [7] - Grafos
# [8] - Geometria Computacional
# [9] - SQL
'''
categoria = 3


'''
Organização (forma como é ordenado)
[1] - Ordem crescente (numero)
[2] - Ordem crescente (dificuldade/nível)
'''
organizacao = 2


'''
Quantos = Separação de exercicios (Lista completa = 0)
Exemplo: 2
1001 1002
1003 1004
Exemplo: 3
1001 1002 1003
1004 1005 1006
'''
quantos = 0

'''
Dificuldade
Imprimir com dificuldade?
[1] - Sim
[2] - Nao
'''
dificuldade = 0
lista_completa = manipulacao_arquivo(categoria)

if(organizacao == 1):
    print_categoria(categoria)
    ordenacao_exercicio(dificuldade,lista_completa)
if(organizacao == 2):
    print_categoria(categoria)
    ordenacao_dificuldade(lista_completa,quantos)



