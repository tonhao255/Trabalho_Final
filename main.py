from pessoa import Pessoa
from elfo import Elfo
from claus import Claus
from crianca import Crianca
from presente import Presente
import csv
from pathlib import Path
import os
import pygame
import time

bg_music = "jingle_my_bells.mp3"
error_snd = "metal_pipe.mp3"

pygame.mixer.init()
pygame.mixer.music.load(bg_music)
pygame.mixer.music.play(loops=-1, start=0)

def error(error_msg:str):
    print(str(error_msg))
    pygame.mixer.music.load(error_snd)
    pygame.mixer.music.play(loops=1, start=0)
    time.sleep(3)
    pygame.mixer.music.load(bg_music)
    pygame.mixer.music.play(loops=-1, start=0)

os.system('cls' if os.name == 'nt' else 'clear')
print('''         |
        -+-
         A
        /=\\         
      i/ O \\i   
      /=====\\      |,\\/,| |[_' |[_]) |[_]) \\\\//
      /  i  \\      ||\\/|| |[_, ||'\\, ||'\\,  ||
    i/ O * O \\i    
    /=========\\      ___ __ __ ____  __  __  ____  _  _    __    __
    /  *   *  \\     // ' |[_]| |[_]) || ((_' '||' |,\\/,|  //\\\\  ((_'
  i/ O   i   O \\i   \\\\_, |[']| ||'\\, || ,_))  ||  ||\\/|| //``\\\\ ,_))
  /=============\\  
  /  O   i   O  \\  
i/ *   O   O   * \\i
/=================\\
       |___|''')    
time.sleep(2)

data = Path("data")
if not data.is_dir():
    os.mkdir("data")

claus = Path("data\\claus.csv")
if not claus.is_file():
    claus = open("data\\claus.csv", "a")

elfo = Path("data\\elfo.csv")
if not elfo.is_file():
    elfo = open("data\\elfo.csv", "a")

crianca = Path("data\\crianca.csv")
if not crianca.is_file():
    crianca = open("data\\crianca.csv", "a")

presente = Path("data\\presente.csv")
if not presente.is_file():
    presente = open("data\\presente.csv", "a")

while(True):
    wrong = 0
    os.system('cls' if os.name == 'nt' else 'clear')

    print("\n-------Welcome to the Jolly System-------")
    print("Selecione serviço: ")
    print("1 - Edição de Elfo")
    print("2 - Edição de Criança")
    print("3 - Edição de Presentes")
    print("4 - Edição de Claus")

    try:
        slct_servico = int(input("--->"))
        if slct_servico > 4 or slct_servico < 1:
            raise ValueError
    except:
        error("Opção inválida, tente novamente.") # <--- função interna criada lá em cima
        wrong = 1
    

    if wrong == 0:
        print("ok")
        time.sleep(1)
        if slct_servico == 1:
            
            lista_elfos = []
            with open(elfo, 'r') as file:
                myFile = csv.reader(file, delimiter=",")
                for row in myFile:
                    try:
                        lista_elfos.append(Elfo(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5])))
                    except:
                        error("Erro ao carregar dados do arquivo.")
                        wrong = 1
                    
            if wrong == 0:
                slct_print = input("Imprimir Elfos? digite 1: ")
                
                if slct_print == "1":
                    j = 0
                    for i in lista_elfos:
                        j += 1
                        print("")
                        print(f"------Elfo N°{j}------")
                        print(i)

                print("")
                print("---------Seleção----------")
                print("selecione elfo por número (0 cancela)")

                #try:
                if True:
                    print(len(lista_elfos))
                    slct_individuo = int(input("--->"))

                    if slct_individuo == 0:
                        pass
                    elif slct_individuo > len(lista_elfos) or slct_individuo < 1:
                        raise ValueError
                    individuo = lista_elfos[slct_individuo - 1]
                    print(type(individuo))
                    print(individuo)
                    print(f"\n-------Editando {lista_elfos[slct_individuo - 1].get_nome}-------")
                    print("Escolha o que vai editar (0 cancela): ")
                    print("1 - Nome")
                    print("2 - Sobrenome")
                    print("3 - Idade")
                    print("4 - Endereço")
                    print("5 - Especialidade")
                    print("6 - Departamento")
                    if True:
                        slct_opcao = int(input("--->"))
                        if slct_opcao == 0:
                            pass #pra lembrar que 0 é cancelar
                            
                        elif slct_opcao > 6 or slct_opcao < 1:
                            raise ValueError
                        
                        if slct_opcao == 1:
                            novo = input("Insira novo nome: ")
                            individuo.set_nome = novo

                        if slct_opcao == 2:
                            novo = input("Insira novo sobrenome: ")
                            individuo.set_sobrenome = novo
                        
                        if slct_opcao == 3:
                            novo = input("Insira nova idade: ")
                            individuo.set_idade = novo

                        if slct_opcao == 4:
                            novo = input("Insira novo endereço: ")
                            individuo.set_endereco = novo

                        if slct_opcao == 5:
                            novo = input("Insira nova especialidade: ")
                            individuo.set_especialidade = novo
                        
                        if slct_opcao == 6:
                            novo = input("Insira novo departamento: ")
                            individuo.set_departamento = novo

                        lista_elfos[slct_individuo - 1] = individuo

                        with open('data\\elfo.csv', 'w+', newline='') as file:
                            myFile = csv.writer(file)
                            for i in range(len(lista_elfos)):
                                myFile.writerow(lista_elfos[i].row())

                    # except:
                    #     print(1)
                    #     error("Opção inválida, tente novamente.")
                        

                #except:
                    # print(2)
                    # error("Opção inválida, tente novamente.")


# with open(data) as data:
#     reader = csv.reader(data, delimiter=',')
#     for i in reader:
#         try:
#             print(f'number: {i[0]} \nnumber: {i[1]} \nnumber: {i[2]} \nnumber: {i[3]}\n')
#         except:
#             print("não foi possivel realizar a mostra de dados, o arquivo pode estar corrompido!")
#             pygame.mixer.music.play(loops=2, start=0)
#             print("yeah")
#             time.sleep(3)