    
class PlanoTelefone:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo


    
class UsuarioTelefone:
    def __init__(self,nome,plano):
        self.nome = nome
        self.plano = plano

    def verificar_saldo(self,saldo):

        if saldo < 10:
            mensagem_personalizada = "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
            return mensagem_personalizada
        elif saldo >= 50:
            mensagem_personalizada = "Parabéns! Continue aproveitando seu plano sem preocupações."
            return mensagem_personalizada
        else:
            mensagem_personalizada = "Seu saldo está razoável. Aproveite o uso moderado do seu plano."
            return f'{mensagem_personalizada}'    

# Entrada:
nome_usuario = input()
nome_plano = input()
saldo_inicial = float(input())

plano_usuario = PlanoTelefone(nome_plano, saldo_inicial) 
usuario = UsuarioTelefone(nome_usuario, plano_usuario)  

saldo_usuario = usuario.verificar_saldo(saldo_inicial)  
print(saldo_usuario)