#Criptografando e descriptografando um numero e/ou senha
n = str(input('Digite um inteiro de 4 digitos: '))
#criptografa o numero

d1 = str((int(n[0])+6) % 10) # novo digito1 = (digito1 + 6)%10
d2 = str((int(n[1])+6) % 10) # novo digito2 = (digito2 + 6)%10
d3 = str((int(n[2])+6) % 10) # novo digito3 = (digito3 + 6)%10
d4 = str((int(n[3])+6) % 10) # novo digito4 = (digito4 + 6)%10


d2.replace(' ','0')
d3.replace(' ','0')
d4.replace(' ','0')
#Agora trocara a posicao do novo d1 pela posicao do novo d3 e faz o mesmo para d2 e d4
numerocriptografado = d3+d4+d1+d2
numerocriptografado.replace(' ','0')

print("Numero criptografado: " + numerocriptografado)

cript = str(input('Digite o numero criptografado: '))

#Descriptografa o numero obtido acima ...
dd1 = str((int(cript[2]) + 4) % 10)
dd2 = str((int(cript[3]) + 4) % 10)
dd3 = str((int(cript[0]) + 4) % 10)
dd4 = str((int(cript[1]) + 4) % 10)

descriptografado = dd1 + dd2+ dd3+dd4
descriptografado.replace(' ','0')
print('Numero Original: ' + descriptografado)

            
