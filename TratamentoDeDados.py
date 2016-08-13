# -*- coding: UTF-8 -*-
import re
import fileinput


# retira caracteres especiais da palavra
def limpaCaracteres(linha_suja):        # Função que usa expressões regulares para limpar os dados originais
    linha_suja = linha_suja.lower().strip()
    linha_suja = re.sub("&.{2,4};", " ", linha_suja)
    linha_suja = re.sub("\\{\\{!\\}\\}", " ", linha_suja)
    linha_suja = re.sub("{{.*?}}", " ", linha_suja)
    linha_suja = re.sub("<docno>", " <docno> ", linha_suja)
    linha_suja = re.sub("ref", " ", linha_suja)
    linha_suja = re.sub("[\s,.:;=!?]", " ", linha_suja)
    linha_suja = re.sub("[\/]", " ", linha_suja)
    linha_suja = re.sub("[\[*]", " ", linha_suja)
    linha_suja = re.sub("[\]*]", " ", linha_suja)
    linha_suja = re.sub("[\|*]", " ", linha_suja)
    linha_suja = re.sub("[\{*]", " ", linha_suja)
    linha_suja = re.sub("[\}*]", " ", linha_suja)
    linha_suja = re.sub("[\'*#()_]", " ", linha_suja)
    linha_suja = re.sub("jpg", " ", linha_suja)
    linha_suja = linha_suja.replace("<doc>", " ")
    linha_suja = linha_suja.replace("<p>", " ")
    linha_suja = linha_suja.replace("<root>", " ")
    linha_suja = linha_suja.replace("< doc>", " ")
    linha_suja = linha_suja.replace("< p>", " ")
    linha_suja = linha_suja.replace("< root>", " ")
    linha_suja = re.sub('[0-9*]', '', linha_suja)
    return linha_suja

#Limpa cada linha do documento
def limpaArquivo(pathArquivo, pathArquivoNovo):
    arquivoSujo = open(pathArquivo, "r")
    arquivoLimpo= open(pathArquivoNovo+"\\ArquivoLimpo.txt", "w")
    linhaAtual=" "
    while(linhaAtual != ""):
        linhaAtual = arquivoSujo.readline()
        linhaAtual= limpaCaracteres(linhaAtual)
        arquivoLimpo.write(linhaAtual +"\n")
    arquivoSujo.close()
    arquivoLimpo.close()


# sepera os arquivos para analise, elimine o arquivo com numeração 0, ele não faz o arquivo de numero 1000 tem que ser manual
def FazerArquivo(pathArquivo, path):
    indice=0
    texto= ""
    for linhaAtual in fileinput.input(pathArquivo):
        if linhaAtual.split().__contains__('<docno>'):
            arquivoSujo = open(path+"\\"+str(indice)+ ".txt", "w")
            arquivoSujo.write(texto)
            arquivoSujo.close()
            texto= ""
            indice= indice+ 1

        else:
            texto= linhaAtual + texto +"/n"




#execução
#limpaArquivo("C:\\Users\\jordan\\Documents\\ptwiki-v2.txt", "C:\\Users\\jordan\\Documents" ) # so executa 1 vez, tire o comentario para executar

FazerArquivo("C:\\Users\\jordan\\Documents\\ArquivoLimpo.txt", "C:\Users\jordan\Documents\Ri- Textos")


