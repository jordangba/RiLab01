# -*- coding: UTF-8 -*-
import re
from Postings import Postings
from Lexicon import Lexicon
from operator import itemgetter
import math
import fileinput


totalDoc= 1000
dadosRe = {}
valorK= 1.2

#Faz a inserção na hash das palavras dos textos, junto com o calculo da IDF e da frequencia.

def adicicao(dadosRE, palavra, indice):
    palavra = re.sub('[0-9*]', '', palavra)
    if (dadosRE.has_key(palavra)):
        contem= False
        for c in range(len(dadosRe[palavra].getListaPost())):
            if(dadosRe[palavra].getListaPost()[c].getDoc()== indice):
                dadosRe[palavra].getListaPost()[c].setValor(dadosRe[palavra].getListaPost()[c].getValor()+1)
                dadosRe[palavra].setFrequencia(dadosRe[palavra].getFrequencia()+1)
                contem= True
        if(contem==False):
            posting = Postings(indice, 1)
            dadosRe[palavra].getListaPost().append(posting)
            dadosRe[palavra].setFrequencia(dadosRe[palavra].getFrequencia() + 1)
            dadosRe[palavra].setnumeroDoc(dadosRe[palavra].getnumeroDoc()+1)
            dadosRe[palavra].setidf(math.log10((totalDoc+1)/(dadosRe[palavra].getnumeroDoc())))
    else:
        posting = Postings(indice,1)
        lexicon = Lexicon(1,1,0,[])
        type(lexicon.getListaPost())
        lexicon.getListaPost().append(posting)
        lexicon.setidf(math.log10((totalDoc+1)/(lexicon.getnumeroDoc())))
        dadosRe[palavra] = lexicon


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


# Pega a linha de um documento e faz a index Invertido
def FazerIndex(pathArquivo):
    indice=0
    for linhaAtual in fileinput.input(pathArquivo):  # Lê cada linha do arquivo de entrada e depois indexa no dicionari
        if linhaAtual.split().__contains__('<docno>'):
            indice= indice+ 1
        elif linhaAtual.__contains__("<headline>"):
            linhaAtual.replace("<headline>", "")
            linhaAtual.replace("< headline>", "")
            adicicao(dadosRe, linhaAtual, indice)
        else:
            for palavra in  linhaAtual.split():
                adicicao(dadosRe, palavra, indice)
    return dadosRe

# Imprime um arquivo com o Indice Invertido
def colocArquivo(dadosRE, PastaDestino):
    chave = dadosRe.keys()
    arq = open(PastaDestino+"\\IndiceInvertidoIDF.txt", "w")
    for postings in range(len(chave)):
        resposta =""
        for s in range(len(dadosRe[chave[postings]].getListaPost())):
            resposta = resposta + " " + str((str(dadosRe[chave[postings]].getListaPost()[s].getDoc()),str(dadosRe[chave[postings]].getListaPost()[s].getValor()) ))
        arq.write(chave[postings] +" (Numero Documentos: "+str(dadosRe[chave[postings]].getnumeroDoc())+")" + " (Frequencia: "+str(dadosRe[chave[postings]].getFrequencia())+")" +
                  " (IDF: "+str(dadosRe[chave[postings]].getIdf())+")"" :" + resposta + "\n")
    arq.close()


def intersect(palavra1, palavra2, dadosRe):
    cont1 = 0
    cont2 = 0
    resposta = []
    while len(dadosRe[palavra1]) > cont1 and len(dadosRe[palavra2]) > cont2:
        if ((dadosRe[palavra1][cont1]) == (dadosRe[palavra2][cont2])):
            resposta.append(dadosRe[palavra1][cont1])
            if (len(dadosRe[palavra1]) > cont1):
                cont1 = cont1 + 1
            if (len(dadosRe[palavra2]) > cont2):
                cont2 = cont2 + 1
        elif dadosRe[palavra1][cont1] < dadosRe[palavra2][cont2]:
            if (len(dadosRe[palavra1]) > cont1):
                cont1 = cont1 + 1
        else:
            if (len(dadosRe[palavra2]) > cont2):
                cont2 = cont2 + 1
    return resposta

def union(palavra1, palavra2, dadosRe):
    return set(dadosRe[palavra1] + dadosRe[palavra2])

#Calcular o valor da palvra da query em relação a um documento
def valorDaPalavraNoDoc (palavra, dicionario, resultado, quantidade):
    lista = dicionario[palavra].getListaPost()
    for i in range(len(lista)):
        if(resultado.has_key(lista[i].getDoc())):
            resultado[lista[i].getDoc()]= resultado[lista[i].getDoc()]+ CalculoDoValorDaPalavra(1, ((lista[i].getValor()* (valorK+1))/(lista[i].getValor()+ valorK+1)) ,dicionario[palavra].getIdf())

        else:
            resultado[lista[i].getDoc()] = CalculoDoValorDaPalavra( 1, ((lista[i].getValor() * (valorK+1))/(lista[i].getValor() + valorK+1)), dicionario[palavra].getIdf())




# Faz o rank dos documento em relação a query passada
def rank (query, dicionario):

    resultado={}
    resposta =""
    lista= query.split(" ")
    for i in range(len(lista)):
        valorDaPalavraNoDoc(lista[i], dicionario, resultado, 1)
    resultado= sorted(resultado.items(), key= itemgetter(1), reverse=True)
    for i in range(5):
        resposta= resposta + "Documento: "+str(resultado[i][0]) +" "+ "Posicao: "+ str(i+1) + " "

    return  query +": " +resposta+ "\n"


def CalculoDoValorDaPalavra (quantidadePalavra, quantidadePalavraDocumento, idfPalavra ):
    return quantidadePalavra*(quantidadePalavraDocumento*idfPalavra)