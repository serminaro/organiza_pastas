###########################################################################################
#==                     GAMBOA CONSULTORIA EDUCACIONAL                                  ==#
#==                                                                                     ==#
#==   DATA DE CRIAÇÃO:       01.02.2022                                                 ==#
#==   DATA ULTIMA ALTERAÇÃO: 17.01.2023                                                 ==#
#==   VERSÃO: Python 3.8           Interpretador IDLE                                   ==#
#==   AUTOR: SERMINARO,B.A.C.(Bruno Serminaro)                                          ==#
#==   E-MAIL:bruno.serminaro@gmail.com                                                  ==#
###########################################################################################
#= Script que cria a pasta e as subpastas necessárias para organização dos
#= pedidos de orçamento do laboratório de acustica. E uma possível evolução
#= é ele copiar um arquivo padrão do texto do orçamento.
###########################################################################################
def maiuscula(string):
    retorno = ''
    for caractere in string:
        retorno += caractere.upper()
    return retorno
        

#--------------------- IMPORTANDO OS PACOTES UTILIZADOS ----------------------------------#
import os         #pacote de sistema operacional
import sys        #pacote padrão
import glob       #pacote que le conteúdo de pastas
import subprocess #pacote que permite rodar outros processos de dentro python

#------------------------ DECLARAÇÃO DE VARIAREIS-----------------------------------------#
#pastaDestino  = 'D:\\Programacao\\Teste\\Cria_Pasta_de_Professor_Rev01'
pastaDestino   = ''
pastaLeitura   = 'nada'
pastaEscrita   = []
pastaEscritaA  = []
pastaEscritaAA = []
pastaEscritaB  = []
pastaEscritaBB = []
pastaEscritaC  = []
temp =[]

#------------------------------------------------------------------------------------------#
inf = ["ano","escola","disciplina","ciclo","serie","turma","aulas_semana"];
subPastas= ['planos_de_aula','cadernos_e_materiais','acompanhamentos'];
subPastasA=['aula','material','acomp'];
subPastasB=['Fixacao','Prova','Repositorio'];


#---------------------------INICIO DE CICLO-------------------------------------------------#
print('|===============================================================================|')
print('|                       E. E. Santa Dalmolin                                    |')      
print('|                     Fundamental Series Finais                                 |')
print('|                                                                               |')       
print('| DATA ULTIMA ALTERAÇÃO: 01.02.2022                                             |')                                   
print('|AUTOR: SERMINARO,B.A.C.  E-MAIL:serminaro@prof.educacao.sp.gov.br              |')
print('|===============================================================================|')
print('| Programa para criar pastas e subpastas modelo padrão para os                  |')
print('| professores da escola santa dalmolin                                          |')
print('= Você está trabalhando na pasta:                                               |')
print('= ' + os.getcwd() + '           ')                                
print('|===============================================================================|')
print('|===============================================================================|')

escolha_pasta = input("Deseja trocar o diretorio de criacao? (S ou (N) ) : ")  
if escolha_pasta == "S" or escolha_pasta == "s" :
    pastaDestino = input("Digite o endereco do diretorio : ")
    os.chdir(pastaDestino);                                                                #Comando que troca o diretorio onde o programa está lendo
    arquivos =glob.glob("*")                                                               #Comando glob varre a pasta 
    print('= Você está trabalhando na pasta: |')
    print('= ' + os.getcwd() + '           ') 
    print('= Os arquivos presentes na pasta sao: |')
    for i in range(len(arquivos)):
        print(arquivos[i])
if escolha_pasta == "n" or escolha_pasta == "N":
    pastaDestino = os.getcwd()

#============================= COMEÇO DO PROGRAMA PRINCIPAL======================            
for i in range(len(inf)):
    inf[i] = input("insira os dados de " + inf[i] + " de "+": ")

print("\n As pastas a serem criadas seguem abaixo:")

pastaEscrita.append(inf[0] +"_"+"["+ maiuscula(inf[1]) +"]"+"_"+inf[2][:3]+"_"+ maiuscula(inf[3]) +"_"+inf[4]+"a"+ maiuscula(inf[5]))

for j in range(len(subPastas)):
    pastaEscrita.append(inf[0] +"_"+"["+ maiuscula(inf[1]) +"]"+"_"+inf[2][:3]+"_"+ maiuscula(inf[3]) +"_"+inf[4]+"a"+ maiuscula(inf[5]) + "_" + subPastas[j])

    print(pastaEscrita)

#------Plano de aula----------------
for j in range(1,5):
    pastaEscritaA.append(inf[0] +"_"+"["+ maiuscula(inf[1][:3]) +"]"+"_"+inf[2][:3]+"_"+ maiuscula(inf[3]) +"_"+inf[4]+"a"+ maiuscula(inf[5]) + "_" +str(j) +"BIM_"+ subPastasA[0] )
#pastaEscritaA.append(inf[0] +"_"+"["+ maiuscula(inf[1][:3]) +"]"+"_"+inf[2][:3]+"_"+ maiuscula(inf[3]) +"_"+inf[4]+"a"+ maiuscula(inf[5]) + "_" + "LEGADO_" + subPastasA[0] )
for i in range(len(pastaEscritaA)):
    print(pastaEscritaA[i])

for k in range(len(pastaEscritaA)):
    if k == 0:
        for j in range(100,100+(int(inf[6])*10)):
            temp.append( pastaEscritaA[k] +str(j) )
    if k == 1:
        for j in range(200,200+(int(inf[6])*10)):
            temp.append( pastaEscritaA[k] +str(j))
    if k == 2:
        for j in range(300,300+(int(inf[6])*10)):
            temp.append( pastaEscritaA[k] +str(j) )
    if k == 3:
        for j in range(400,400+(int(inf[6])*10)):
            temp.append( pastaEscritaA[k] +str(j) )

    pastaEscritaAA.append(temp)
    temp = []

for i in range(len(pastaEscritaAA)):
    for j in range(len(pastaEscritaAA[i])):
        print(pastaEscritaAA[i][j])
    
    

#-------Material
for j in range(1,5):
    pastaEscritaB.append(inf[0] +"_"+"["+ maiuscula(inf[1][:3]) +"]"+"_"+inf[2][:3]+"_"+ maiuscula(inf[3]) +"_"+inf[4]+"a"+ maiuscula(inf[5]) + "_" + str(j) +"BIM_"+ subPastasA[1] )

for k in range(len(pastaEscritaB)):
    for j in range(len(subPastasB)):
        temp.append( pastaEscritaB[k] +"_"+ subPastasB[j] )
    pastaEscritaBB.append(temp)
    temp = []


for i in range(len(pastaEscritaB)):
    print(pastaEscritaB[i])
for i in range(len(pastaEscritaBB)):
    for j in range(len(pastaEscritaBB[i])):
        print(pastaEscritaBB[i][j])


#-----Acompanhamento
for j in range(1,5):
    pastaEscritaC.append(inf[0] +"_"+"["+ maiuscula(inf[1][:3]) +"]"+"_"+inf[2][:3]+"_"+ maiuscula(inf[3]) +"_"+inf[4]+"a"+ maiuscula(inf[5]) + "_" + str(j) +"BIM_"+ subPastasA[2] )
for i in range(len(pastaEscritaC)):
    print(pastaEscritaC[i])

#------------------------------------------

os.mkdir(pastaEscrita[0])
pastaLeitura = os.getcwd()+ "\\" + pastaEscrita[0]
os.chdir(pastaLeitura)
print(os.getcwd())
for i in range(1,len(pastaEscrita)):
    os.mkdir(pastaEscrita[i])

#-----------------------
os.chdir(pastaLeitura +"\\" + pastaEscrita[1])
for i in range(len(pastaEscritaA)):
    os.mkdir(pastaEscritaA[i])
  
os.chdir(pastaLeitura +"\\" + pastaEscrita[1]+"\\"+pastaEscritaA[0])
for i in range(len(pastaEscritaAA[0])):
    os.mkdir(pastaEscritaAA[0][i])

os.chdir(pastaLeitura +"\\" + pastaEscrita[1]+"\\"+pastaEscritaA[1])
for i in range(len(pastaEscritaAA[1])):
    os.mkdir(pastaEscritaAA[1][i])

os.chdir(pastaLeitura +"\\" + pastaEscrita[1]+"\\"+pastaEscritaA[2])
for i in range(len(pastaEscritaAA[2])):
    os.mkdir(pastaEscritaAA[2][i])

os.chdir(pastaLeitura +"\\" + pastaEscrita[1]+"\\"+pastaEscritaA[3])
for i in range(len(pastaEscritaAA[3])):
    os.mkdir(pastaEscritaAA[3][i])



os.chdir(pastaLeitura + "\\" + pastaEscrita[2])
for j in range(len(pastaEscritaB)):
    os.mkdir(pastaEscritaB[j])
os.chdir(pastaLeitura +"\\" + pastaEscrita[2]+"\\"+pastaEscritaB[0])
for i in range(len(pastaEscritaBB[0])):
    os.mkdir(pastaEscritaBB[0][i])

os.chdir(pastaLeitura +"\\" + pastaEscrita[2]+"\\"+pastaEscritaB[1])
for i in range(len(pastaEscritaBB[1])):
    os.mkdir(pastaEscritaBB[1][i])

os.chdir(pastaLeitura +"\\" + pastaEscrita[2]+"\\"+pastaEscritaB[2])
for i in range(len(pastaEscritaBB[2])):
    os.mkdir(pastaEscritaBB[2][i])

os.chdir(pastaLeitura +"\\" + pastaEscrita[2]+"\\"+pastaEscritaB[3])
for i in range(len(pastaEscritaBB[3])):
    os.mkdir(pastaEscritaBB[3][i])

os.chdir(pastaLeitura + "\\" + pastaEscrita[3])
for k in range(len(pastaEscritaC)):
    os.mkdir(pastaEscritaC[k])



        


   
 #       pastaEscrita  = []
 #       pastaEscritaA = []
  #      pastaEscritaAA = []
  #      pastaEscritaB = []
  #      pastaEscritaBB = []
   #     pastaEscritaC = []
    #    temp =[]


        
