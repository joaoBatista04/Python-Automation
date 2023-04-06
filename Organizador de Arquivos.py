import os
import time
import shutil

#Definicao do caminho do arquivo e criacao da lista de arquivos
caminho = r"C:\Users\joaop\OneDrive\Imagens\Camera"
lista_arquivos = os.listdir(caminho)

#Loop principal
for arquivo in lista_arquivos:
    #Acesso do caminho atual e obtencao da data de modificacao do arquivo
    caminhoAtual = f"{caminho}\{arquivo}"
    ti_c = os.path.getmtime(caminhoAtual) 
    c_ti = time.ctime(ti_c)

    #Divisao da string de data e formacao de uma nova com dia, mes e ano
    datas = c_ti.split()
    dataAtual = f"{datas[4]}-{datas[1]}-{datas[2]}"

    #Se o diretorio com a data do arquivo nao existir, ele entao eh criado
    if not(os.path.isdir(f"{caminho}\{dataAtual}")):
        os.mkdir(f"{caminho}\{dataAtual}")

    #O arquivo eh movido para o diretorio nomeado com a respectiva data
    shutil.move(f"{caminho}\{arquivo}", f"{caminho}\{dataAtual}")
