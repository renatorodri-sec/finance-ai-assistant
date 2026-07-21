class Contexto:
    def __init__(self):
        self.historico = []

    def adicionar_mensagem(self, usuario, mensagem):
        self.historico.append({
            "usuario": usuario,
            "mensagem": mensagem
        })

    def obter_historico(self):
        return self.historico

    def limpar(self):
        self.historico = []
