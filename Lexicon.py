# -*- coding: UTF-8 -*-
#A classe guarda a NumeroDoc= a quantidade de documento que a palavra aparece
#Frequencia = o Numero total que a palavra em questão aparece no total de documentos
# idf= idf da palavra em questão
#ListaPost = Lista de postings que as palavras possuem
class Lexicon:

    def __init__(self, numeroDoc, frequencia, idf, listaPost ):
        self.numeroDoc= numeroDoc
        self.frequencia= frequencia
        self.idf= idf
        self.listaPost= listaPost


    def getnumeroDoc(self):
        return self.numeroDoc


    def getFrequencia(self):
        return self.frequencia

    def getIdf(self):
        return self.idf

    def getListaPost(self):
        return self.listaPost

    def setnumeroDoc(self, numeroDocNovo):
        self.numeroDoc= numeroDocNovo

    def setFrequencia(self, frequenciaNova):
        self.frequencia= frequenciaNova

    def setidf(self, idfNova):
        self.idf= idfNova