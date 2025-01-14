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


pygame.mixer.init()
pygame.mixer.music.load("C:\\Users\\Suporte\\Documents\\Trabalho_Final-main\\jingle_my_bells.mp3")
pygame.mixer.music.play(loops=-1, start=0)

data = Path(str(os.path.realpath(__file__))[0:-7] + "\\data")
if not data.is_dir():
    os.mkdir("data")

claus = Path(str(os.path.realpath(__file__))[0:-7] + "\\data\\claus.csv")
if not claus.is_file():
    claus = open("data\\claus.csv", "a")

elfo = Path(str(os.path.realpath(__file__))[0:-7] + "\\data\\elfo.csv")
if not elfo.is_file():
    elfo = open("data\\elfo.csv", "a")

crianca = Path(str(os.path.realpath(__file__))[0:-7] + "\\data\\crianca.csv")
if not crianca.is_file():
    crianca = open("data\\crianca.csv", "a")

presente = Path(str(os.path.realpath(__file__))[0:-7] + "\\data\\presente.csv")
if not presente.is_file():
    presente = open("data\\presente.csv", "a")

while(True):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('''         |
        -+-
         A
        /=\\         
      i/ O \\i   
      /=====\\      |,\/,| |[_' |[_]) |[_]) \\\\//
      /  i  \\      ||\/|| |[_, ||'\, ||'\,  ||
    i/ O * O \\i    
    /=========\\      ___ __ __ ____  __  __  ____  _  _    __    __
    /  *   *  \\     // ' |[_]| |[_]) || ((_' '||' |,\/,|  //\\\\  ((_'
  i/ O   i   O \i   \\\\_, |[']| ||'\, || ,_))  ||  ||\/|| //``\\\\ ,_))
  /=============\\  
  /  O   i   O  \\  
i/ *   O   O   * \\i
/=================\\
       |___|''')    
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n-------Welcome to the Jolly System-------")
    print("Selecione serviço: ")
    print("1 - Edição de Elfo")
    print("2 - Edição de Criança")
    print("3 - Edição de Presentes")
    print("4 - Edição de Claus")

    try:
        n = int(input("--->"))
        if n > 4 or n < 1:
            raise ValueError
    except:
        print("Opção inválida, tente novamente.")
        pygame.mixer.music.load("C:\\Users\\Suporte\\Documents\\Trabalho_Final-main\\metal_pipe.mp3")
        pygame.mixer.music.play(loops=1, start=0)
        time.sleep(3)
        pygame.mixer.music.load("C:\\Users\\Suporte\\Documents\\Trabalho_Final-main\\jingle_my_bells.mp3")
        pygame.mixer.music.play(loops=-1, start=0)
    
    if n == 1:
        
        o = input("Imprimir Elfos? digite 1: ")
        if o == "1":
            with open(elfo) as elfo_data:
                elfo_reader = csv.reader(elfo_data, delimiter=',')
                j = 0
                for i in elfo_reader:
                    j += 1
                    print(j)
                    try:
                        print(f'Nome: {i[0]} \nSobrenome: {i[1]} \nIdade: {i[2]} \nEndereco: {i[3]} \nEspecialidade: {i[4]} \nDepartamento: {i[5]}')
                        p = int(input("Selecione um Elfo: "))
                    except:
                        print("não foi possivel realizar a mostra de dados, o arquivo pode estar corrompido!")
                        pygame.mixer.music.load("C:\\Users\\Suporte\\Documents\\Trabalho_Final-main\\metal_pipe.mp3")
                        pygame.mixer.music.play(loops=1, start=0)
                        time.sleep(3)


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