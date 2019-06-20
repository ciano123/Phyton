#Metodo que opera o tamanho em Bytes..
def toMB(tamBytes):
   tamBytes = float(tamBytes)
   return (float(tamBytes/(1024*1024)))

#Metodo que opera a porcentagem...  
def PercentualUs(lista, total):
   percentual = (lista[3]/total)*100
   lista.insert((len(cUsuario)),percentual)

#Metodo que opera a media de espaco ocupado
def MediaOc(lista, total):
   media = 0
   elementos = len(lista)
   media = (total)/(elementos+1)
   return media

#Funcao Main 
cliente = []
posi = 1
total = 0
media = 0
with open ("usuarios.txt","r") as arquivo:
   valor = 0
   for linha in arquivo:
      cliente.append(linha.split()) 

   for cUsuario in cliente:
      cUsuario.insert(0,posi)
      valor = toMB(float(cUsuario[2]))
      total += valor
      cUsuario.insert((len(cUsuario)),valor)
      posi+=1

   for cUsuario in cliente:
      PercentualUs(cUsuario, total)

media = MediaOc(cUsuario,total)

with open ("relatorio.txt","w") as arquivo:
   arquivo.write("-------------------------------------------------------------- \n")
   arquivo.write("ACME Inc.         Uso do espaço em disco pelos usuários.\n")
   arquivo.write("--------------------------------------------------------------\n")
   arquivo.write("Nr.\tUsuário        \tEspaço utilizado\t% do uso\n\n")

   for cUsuario in cliente:
      percentagem="{0:.2f}".format(round(cUsuario[3],2))
      arquivo.write(str(cUsuario[0])+'\t'+"{:<15}".format(cUsuario[1])+'\t'+"{:<16}".format(percentagem)+'MB'+'\t'+"{0:.2f}".format(cUsuario[4])+'%'+'\n')

   arquivo.write('\n\nEspaço Total Ocupado: ' + "{0:.2f}".format(total) + ' MB')
   arquivo.write('\n\nEspaço médio Ocupado: ' + "{0:.2f}".format(media) + ' MB')
   arquivo.close()

with open ("relatorio.txt","r") as arquivo:
   print(arquivo.read())
