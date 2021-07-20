## Agent

class Agent:
    def self_play(self):
        """ Cria um training set. Em cada movimento, guardar:
                1. o estado do jogo
                2. as search probabilities (do MCTS)
                3. o value (quando o jogo acaba)
        """

    def retrain_network(self):
        """ Usando o training set criado em self_play, otimiza os pesos da rede neural (model.py)
            Em um loop, retreinar de uma forma mais ou menos actor-critic ocm a funcao
            l = (z-v)^2 + pi*log(p) + c*mod(theta)^2
        """

    def evaluate_network(self):
        """" Teste para ver se a rede resultado de retrain_network eh melhor que a ultima.
             Jogar x jogos entre as duas e substituir a melhor pela ganhadora.
        """