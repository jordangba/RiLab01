# coding: utf-8

import Lab01RI

dicionario= {}
dicionario= Lab01RI.arrumaDocumento("C:\Users\jordan\Documents\ptwiki-v2.txt", "C:\Users\jordan\Desktop\stopwords.txt")
Lab01RI.colocArquivo(dicionario, "C:\Users\jordan\Documents")

print(Lab01RI.intersect("bíblicos", "nomes", dicionario))

print(Lab01RI.union("bíblicos", "nomes", dicionario))

print(Lab01RI.intersect("estados", "unidos", dicionario))

print(Lab01RI.union("estados", "unidos", dicionario))

print(Lab01RI.intersect("winston", "churchill", dicionario))

print(Lab01RI.union("winston", "churchill", dicionario))
