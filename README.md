# Trabalho-Phyton
Autor:

Nome: Francisco Cassiano de Vasconcelos Souza   Matrícula: 413067

E-mail: casinho.555@gmail.com Curso: Engenharia de Computação

Instituição: Universidade Federal do Ceará (Campus Sobral).

Descrição do Trabalho: 

Escolhendo 3 das 4 questões propostas para solucionar com a linguagem Python.

#01) Questão: 
Foi dado um problema em que queria saber o espaço ocupado pelos usuários, e identificar os usuários com mais espaço ocupado,
através de um arquivo chamado “usuários.txt”. Os dados deviam ser reproduzidos em Megabytes em outro arquivo chamado “relatório.txt” e dando também o percentual de uso de cada um.

Primeiramente foi criado métodos para operar no programa. O primeiro chamado “toMB” responsável por calcular o tamanho em conversão de Bytes para MegaBytes. O segundo chamado “PercentualUs”, responsável por calcular o percentual de uso de cada usuário. E um terceiro método “MediaOc” que calcula a media de ocupação do espaço utilizado.
 	Após a criação dos métodos criou-se uma função Main responsável pela execução da operação e chamada dos métodos. Utilizando series de repetições para leitura dos dados e operando sobre eles os métodos criados acima. Logo depois utilizou-se operações para escrever os dados atualizados no novo arquivo “relatório.txt”. 
Executando com o “F5” é mostrado na tela os dados listados de cada usuário e a porcentagem de uso, e um total de dados utilizados e a media. 

#02) Questão:
Foi pedido a criação de um programa que criptografe dados de modo que esses fossem transmitidos mais seguramente. São transmitidos como inteiros de 4 dígitos. Foi pedido também a troca do primeiro dígito pelo terceiro e o segundo digito pelo quarto. E depois pediu a descriptografia de modo que imprima o numero original.

Em primeiro momento foi criado a operação de criptografia dos dados recebidos em forma de string. Depois somando + 6 e pegando o resto da divisão por 10 (%10), armazenando em novas variáveis. 
Após isso foi feito a operação de troca de variáveis pondo os novos valores nas posições propostas. 
Logo, foi impresso o novo resultado criptografado.
Em seguida foi criado a operação de descriptografia dos dados digitando os dados criptografados para saber o numero original.

#Executando: 

É pedido ao usuário para digitar um inteiro de quatro dígitos. Em seguida, mostra o numero criptografado. Logo após exibe a mensagem para o usuário digitar o numero criptografado. Digitando o numero correspondente exibirá o numero original.

#3) Questão:
Pede para implementar uma classe chamada Carro com algumas propriedades (métodos): 

Um veículo tem um certo consumo de combustível (medidos em km / litro) e o nível de combustível inicial é 0.

• Método adicionarGasolina( ), responsável por abastecer o tanque.
• Método andar( ) onde simule o ato de dirigir o veículo por uma certa distância (dist), reduzindo o nível de combustível no tanque de gasolina.
• Método obterGasolina( ) responsável por retorna o nível atual de combustível.

#Executando: 

O usuário deve digitar o nome do carro que receba a classe “Carro”. Logo irá adicionar combustível usando o método adicionarGasolina().Depois deve especificar a quantidade em km que o carro irá andar usando o método andar().Concluindo mostrará a quantidade de combustível usando o método obterGasolina().

Ex: meufusca = Carro(15). Onde 15 será a quantidade de litros que o carro anda por litro de combustível. meuFusca.adicionarGasolina(20). Em que 20 será o total de litros de gasolina adicionado ao tanque. meuFusca.andar(100), em que 100 é quantidade em km que o carro irá percorrer. meuFusca.obterGasolina(), será mostrado a mensagem e valor atual de gasolina. Seguindo o exemplo: Total de combustivel: 13.333333333333332.

