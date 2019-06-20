#Classe carro que contém todos os metodos que o problema propoe
class Carro(object):
    cTanque = 0
    def __init__(self, combL):
        self.combL = combL
        
#Metodo AdicionarGasolina: Responsavel por atualizar a quantidade de gasolina
    def adicionarGasolina(self, adiTanque):
            self.__class__.cTanque = self.__class__.cTanque + adiTanque #Adiciona combustivel ao tanque.
#Metodo andar: Recebe uma quantidade em quilometros que o carro terá que andar            
    def andar(self, dist):
            self.dist = dist/self.combL #Calcula a quantos litros sao percorrido a uma distancia
            self.__class__.cTanque = self.__class__.cTanque - self.dist #Subtrai o combustivel atual pelo utilizado
#Metodo onterGasolina: Imprime a quantidade atualizade de combustivel
    def obterGasolina(self):
               print('Total de combustivel: ',self.cTanque)
        
