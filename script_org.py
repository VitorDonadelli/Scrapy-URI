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

def ordenacao_dificuldade(lista_completa):
    
    dificuldades = []
    exercicios = []
    
    for i in range(1,len(lista_completa),2):
        dificuldades.append(lista_completa[i])
    for i in range(0,len(lista_completa),2):
        exercicios.append(lista_completa[i])
    
    for i in range(0,len(exercicios)):
        for j in range(0,len(exercicios)-1):
            if(dificuldades[j] > dificuldades[j+1]):
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

def ordenacao_exercicio(dificuldade,lista_completa):
    
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

categoria = int(input("Qual categoria quer filtrar?\n[1] - Iniciante\n[2] - AD-HOC\n[3] - Strings\n[4] - Estruturas e Bibliotecas\n[5] - Matemática\n[6] - Paradigmas\n[7] - Grafos\n[8] - Geometria Computacional\n[9] - SQL\n\n"))
lista_completa = manipulacao_arquivo(categoria)



organizacao = int(input("[1] - Ordem crescente (numero)\n[2] - Ordem crescente (dificuldade/nível)\n\n"))
if(organizacao == 1):
    dificuldade = int(input("Imprimir com dificuldade?\n[1] - Sim\n[2] - Nao\n\n"))
    print_categoria(categoria)
    ordenacao_exercicio(dificuldade,lista_completa)
if(organizacao == 2):
    print_categoria(categoria)
    ordenacao_dificuldade(lista_completa)
