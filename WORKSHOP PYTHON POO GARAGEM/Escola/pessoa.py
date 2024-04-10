class Pessoa:
    def __init__(self,nome:str,idade:int,altura:float,cpf:str):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.cpf = cpf

    def dormir(self):
        return f'{self.nome} está dormindo.'
