class Investimento:
    def __init__(self, categoria, tipo, aporte, rentabilidade, periodo_rentabilidade):
        self.Categoria = categoria
        self.Tipo = tipo
        self.Aporte = aporte
        self.Rentabilidade = rentabilidade
        self.Periodo_rentabilidade = periodo_rentabilidade

class Carteira_investimentos:
    def carteira_investimentos(self, investimento, quantidade, rentabilidade_mensal, rentabilidade_anual):
        self.Investimento = investimento
        self.Quantidade = quantidade
        self.Rentabilidade_mensal = rentabilidade_mensal
        self.Rentabilidade_anual = rentabilidade_anual
