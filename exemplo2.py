# -*- coding: UTF-8 -*-
import Lab02



Lab02.limpaArquivo("C:\\Users\\jordan\\Documents\\ptwiki-v2.txt", "C:\Users\jordan\Documents")
dicionario=  Lab02.FazerIndex("C:\Users\jordan\Documents\\ArquivoLimpo.txt")
Lab02.colocArquivo(dicionario, "C:\Users\jordan\Documents")

a=Lab02.rank("primeira guerra mundial", dicionario)
b=Lab02.rank("espaço e tempo", dicionario)
c=Lab02.rank("minha terra tem palmeiras onde canta o sabiá", dicionario)
d=Lab02.rank("grupo raça negra", dicionario)

lista=[]
print a
print b
print c
print d
lista.append(a)
lista.append(b)
lista.append(c)
lista.append(d)


arquivo = open("C:\\Users\\jordan\\Documents\\resposta.txt", "w")

arquivo.writelines(lista)

arquivo.close()