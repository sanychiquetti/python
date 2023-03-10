frase = 'Curso em Vídeo Python'
print(frase[3:13])
print(frase[:6:2])
print(frase[::2])
print(frase.count('o'))
print(frase.upper().count('O')) #aqui estou primeiro colocando tudo em maiúsculo,para achar todas letras O.
print(len(frase))
print(frase.replace('Python', 'HTML')) #ele está apenas printando com a palavra trocada;
print(frase)
#frase = frase.replace('Python', 'Html') #aqui sim estou trocando e substituindo a palavra.
#print(frase)
print('Vídeo' in frase) #vai retornar um booleano, pois estou perguntando se tem a palavra na frase;
print(frase.find('Vídeo')) # vai me retonar com a posição da palavra na frase;
print(frase.lower().find('vídeo')) #estou colocando a palavra toda em minúsculo, para depois ver se tem na frase.
print(frase.split())
dividida = frase.split() # aqui estou colocando em uma variável a frase de forma dividida.
print(dividida[0]) #aqui me mostra apenas a primeira palavra da divisão
print(dividida[2][3]) # aqui vai me mostrar a terceira palavra e a 4 letra da palavra