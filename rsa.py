import math
mensagem=input('digite uma mensagem:')
mens=""
for c in mensagem:
    mens+=str(ord(c))
mens= int(mens)
cprivada1=int(input('digite um número primo para ser sua chave privada:'))
cprivada2=int(input('digite um número primo para ser sua outra chave privada:'))    
n = cprivada1*cprivada2 #chave de decodificação
cop_n= (cprivada1-1)*(cprivada2-1)
chavepublica=int(input(f'digite um número para ser sua chave pública (deve ser coprimo de {cop_n}):'))
a, b = chavepublica, cop_n
while b != 0:
    a, b = b, a % b
if a != 1:
    chavepublica=int(input(f'ocorreu um erro! digite um número para ser sua chave pública (deve ser coprimo de {cop_n}):'))  #essa parte ta cagada n sei calcular mdc
menscodificada= pow(mens, chavepublica, n)
print(f'mensagem codificada: {menscodificada}')




