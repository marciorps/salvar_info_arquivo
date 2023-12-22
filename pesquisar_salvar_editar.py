'''
COMO CRIAR E MODIFICAR ARQUIVOS:
'r' -> usado somente para ler algo
'w' -> usado somente para escrever algo(sempre vai apagar o conteudo anterior)
'r+' -> usado somente para ler e escrever algo
'a' -> usado somente para acrecentar algo
'''

import os

# with open('celulares.txt','w') as arquivo:
#     arquivo.write('celular 2')
# nomes = ['lucas','carol','jeff','douglas']
# with open('nomes.txt','a', newline='', encoding='utf-8') as arquivo:
#     for nome in nomes:
#         arquivo.write(nome + os.linesep)


#desafio - manipulação de arquivos
#Primeiro crie 3 listas
#*uma lista que contém 5 frutas
#*uma lista que contém 5 cores
#*uma lista que contém 5 linguagens de programação
fruta = ['banana','maça','uva','laranja','abacaxi']
cor = ['amarelo','vermelho','branco','preto','azul']
linguagen = ['python','java','c++','javascript','c#']
#Desafio1
##Crie um novo arquivo chamado frutas.txt e insira dentro dele todos as 5 frutas que estão na lista de frutas

with open('frutas.txt','w',newline='', encoding='utf-8') as arquivo:
    for frutas in fruta:
        arquivo.write(frutas + os.linesep)

# #Desafio2
# ##imprima na tela todas as linhas que estão dentro do arquivo fruta.txt
with open('frutas.txt', 'r',newline='',encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(linha)

#desafio3
#Sem apagar os dados que estão dentro de frutas.txt, adicione todas as cores que estão dentro da sua lista de cores ao arquivo fruta.txt
with open('frutas.txt', 'a') as arquivo:
    for cores in cor:
        arquivo.write(os.linesep + cores)

#desafio4
##Crie um novo arquivo chamado 'Top 5 linguagens.txt e popule o arquivo, de forma com que cada linguagem ocupoe apenas uma linha
with open('top 5 linguagens.txt','w',newline='',encoding='utf8') as arquivo:
    for linguagens in linguagen:
        arquivo.write(linguagens + os.linesep)

#Bonus como você poeria criar vários arquivos vazios, usando um laço for?

        
