# -*- coding: UTF-8 -*-
# doc = documento , valor=  frequencia que a palavra aparece no documento em questão
class Postings:

    def __init__(self, doc, valor):
        self.doc=doc
        self.valor= valor


    def getDoc(self):
        return self.doc


    def getValor(self):
        return self.valor

    def setValor(self, valorNovo):
        self.valor= valorNovo