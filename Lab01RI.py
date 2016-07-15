# coding: utf-8
import re

l = ["amp", "lt", "FAQ", "gt", "quot", "ref", "name", "sup", "cox2000", "moore1997", "doi", "Imagem:", "thumb", "jpg",
     "DEFAULTSORT", "fmtn", "px", "LINK", "link", "Link", "wik", "gif"]



dadosRe = {}

#classe que adiciona na Hash os token e os indice, recenbendo o dicionario , palavrava e indice
def adicicao(dadosRE, a, indice):
    if (dadosRE.has_key(a)):
        if dadosRe[a].__contains__(indice) == False:
            dadosRe[a].append(indice)

    else:
        k = []
        k.append(indice)
        dadosRe[a] = k

#quebra a string que contem mais de uma palavra
def quebraPalavra(a, dadosRe, indice):
    l = a.split(" ")
    if (len(l) > 1):
        for i in range(len(l)):
            if (l[i] != ' '):
                adicicao(dadosRe, l[i].lower(), indice)
            else:

                adicicao(dadosRe, l[i].lower(), indice)
    else:
        adicicao(dadosRe, a.lower(), indice)
#retira StopWord da palavra
def tiraStopWord(palavra, listsSW):
    for i in range(len(listsSW)):
        if palavra == listsSW[i].strip():
            return True
    return False

#retirar outrso conjunto de stopword tipica do texto
def tira_lixo(lista, l):
    for i in range(len(l)):
        if lista.__contains__(l[i]):
            return True
    return False

# retirar informções da palavras que vem o "|"
def trata(string, l, indice):
    g = string.split("|")
    for i in range(len(g)):
        if (tira_lixo(g[i], l)) == False and g[i] != "thumb":
            g[i] = cataLixo(g[i])
            quebraPalavra(g[i], dadosRe, indice)

# retira caracteres especiais da palavra
def cataLixo(a):
    a = a.replace(";", " ")
    a = a.replace(".", " ")
    a = a.replace("==", " ")
    a = a.replace("=", " ")
    a = a.replace("“", " ")
    a = a.replace("+", " ")
    a = a.replace("?", " ")
    a = a.replace("!", " ")
    a = a.replace("===", " ")
    a = a.replace("''", " ")
    a = a.replace(":", " ")
    a = a.replace(";", " ")
    a = a.replace(".", " ")
    a = a.replace("==", " ")
    a = a.replace("===", " ")
    a = a.replace("''", " ")
    a = a.replace(":", " ")
    a = a.replace("|", " ")
    a = a.replace("[", " ")
    a = a.replace("]", " ")
    a = a.replace("}", " ")
    a = a.replace("{", " ")
    a = a.replace("*", " ")
    a = a.replace("(", " ")
    a = a.replace(")", " ")
    a = a.replace("--", " ")
    a = a.replace("#", " ")
    a = a.replace("/", " ")
    a = a.replace("'", " ")
    a = a.replace("%", " ")
    a = a.replace(",", " ")
    a = a.replace("-", " ")
    a = a.replace("----", " ")
    a = a.replace("^", " ")
    a = a.replace("<p>", " ")
    a = a.replace("---", " ")
    a = a.replace('/', " ")
    a = re.sub('[0-9*]', '', a)
    a = a.replace("•", " ")
    a = a.replace("—", " ")
    a = a.replace("”", " ")
    a = a.replace("’", " ")
    a = a.replace("…", " ")
    a = a.replace("__", " ")
    a = a.replace("_", " ")
    a = a.replace("↓", " ")
    a = a.replace("—", " ")
    a = a.replace("«", " ")
    a = a.replace("Ø", " ")
    a = a.replace("__________ ", " ")
    a = a.replace("»", " ")
    a = a.replace("<", " ")
    a = a.replace(">", " ")
    a = a.replace("º", " ")
    a = a.replace("ª", " ")

    return a

# Trata a parte do q esta dentro dos <p> do arquivo passado
def arrumaTexto(a, indice, v):
    cont = 0
    while cont < len(a):
        if (a[cont].__contains__("http") or a[cont].__contains__("www")  or a[cont].__contains__("url")):
            cont = cont + 1

        elif (a[cont].find("|") > 0):
            trata(a[cont], l, indice)
            cont = cont + 1


        elif (tira_lixo(a[cont], l)):
            cont = cont + 1

        elif a[cont].__contains__("wik"):
            cont = cont + 1

        elif tiraStopWord(a[cont], v):
            cont = cont + 1
        else:

            a[cont] = cataLixo(a[cont])
            quebraPalavra(a[cont], dadosRe, indice)
            cont = cont + 1


#percorre o arquivo
def arrumaDocumento(stringNomeDiretorio, stringNomedoDiretorioStopWorld ):
    arq2 = open(stringNomeDiretorio, "r")
    stopword = open( stringNomedoDiretorioStopWorld, "r")
    q = arq2.readlines()
    v = stopword.readlines()
    arq2.close()
    stopword.close()
    cont = 0
    indice = 0
    while cont < len(q):
        if q[cont] == "<DOC>":
            cont = cont + 1

        if q[cont].__contains__("<DOCNO>"):
            indice = indice + 1
            cont = cont + 1
        if q[cont].__contains__("HEADLINE"):
            d = q[cont].replace("<HEADLINE>", "")
            d = q[cont].replace("</HEADLINE>", "")
            cont = cont + 1
        if q[cont].__contains__("<P>"):
            cont = cont + 1
            x = arrumaTexto(q[cont].split(), indice,v)
        else:
            cont = cont + 1

    print("fim do inidice")
    return dadosRe




def colocArquivo(dadosRE, PastaDestino):
    h = dadosRe.keys()
    arq = open(PastaDestino+"\\IndiceInvertido.txt", "w")
    for b in range(len(h)):
        for s in range(len(dadosRe[h[b]])):
            v = ""
            v = v + " " + str(dadosRe[h[b]])
        arq.write(h[b] + " :" + v + "\n")
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


