from datetime import datetime
from queue import Queue
from random import randint

class Cliente:
    def __init__(self, nome, tipo_atendimento):
        self.nome = nome
        self.tipo_atendimento = tipo_atendimento
        self.senha_numerica = randint(1000, 9999)
        self.horario_chegada = datetime.now()
        self.horario_atendimento = None
    
    def calcular_tempo_espera(self):
        tempo_espera = (datetime.now() - self.horario_chegada).total_seconds() // 60
        return int(tempo_espera)
    
    def atualizar_estado(self, estado):
        self.horario_atendimento = datetime.now()
        self.estado = estado

class FilaAtendimento:
    def __init__(self, tipo_atendimento, tamanho_maximo):
        self.tipo_atendimento = tipo_atendimento
        self.tamanho_maximo = tamanho_maximo
        self.clientes = Queue(maxsize=tamanho_maximo)
    
    def adicionar_cliente(self, cliente):
        self.clientes.put(cliente)
    
    def remover_cliente(self):
        if not self.clientes.empty():
            return self.clientes.get()
    
    def esta_cheia(self):
        return self.clientes.full()
    
    def esta_vazia(self):
        return self.clientes.empty()

class CaixaAtendimento:
    def __init__(self, tipo_atendimento):
        self.tipo_atendimento = tipo_atendimento
        self.cliente_em_atendimento = None
    
    def chamar_proximo_cliente(self, fila_normal, fila_preferencial):
        if self.tipo_atendimento == "normal":
            if not fila_normal.esta_vazia():
                self.cliente_em_atendimento = fila_normal.remover_cliente()
            elif not fila_preferencial.esta_vazia():
                self.cliente_em_atendimento = fila_preferencial.remover_cliente()
        else:
            if not fila_preferencial.esta_vazia():
                self.cliente_em_atendimento = fila_preferencial.remover_cliente()
            elif not fila_normal.esta_vazia():
                self.cliente_em_atendimento = fila_normal.remover_cliente()
    
    def atualizar_estado(self, estado):
        if self.cliente_em_atendimento:
            self.cliente_em_atendimento.atualizar_estado(estado)
            self.cliente_em_atendimento = None

class SistemaAtendimento:
    def __init__(self, tamanho_fila_normal, tamanho_fila_preferencial):
        self.fila_normal = FilaAtendimento("normal", tamanho_fila_normal)
        self.fila_preferencial = FilaAtendimento("preferencial", tamanho_fila_preferencial)
        self.caixas_normal = [CaixaAtendimento("normal")]
        self.caixas_preferencial = [CaixaAtendimento("preferencial")]
        self.clientes_atendidos = []
    
    def gerar_senha_numerica(self, tipo_atendimento):
        cliente = Cliente(f"Cliente {len(self.clientes_atendidos)+1}", tipo_atendimento)
        if tipo_atendimento == "normal":
            self.fila_normal.adicionar_cliente(cliente)
        else:
            self.fila_preferencial.adicionar_cliente(cliente)
        return cliente.senha_numerica
    
    def abrir_caixa(self, tipo_atendimento):
        if tipo_atendimento == "normal" and len(self.caixas_normal) < 5:
            self.caixas_normal.append(CaixaAtendimento("normal"))
        elif tipo_atendimento == "preferencial" and len(self.caixas_preferencial) < 2:
            self.caixas_preferencial.append(CaixaAtendimento("preferencial"))
    
    def fechar_caixa(self, tipo_atendimento):
        if tipo_atendimento == "normal" and len(self.caixas_normal) > 1:
            self.caixas_normal.pop()
        elif tipo_atendimento == "preferencial" and len(self.caixas_preferencial) > 1:
            self.caixas_preferencial.pop()
    
    def atualizar_caixas(self):
        for caixa in self.caixas_normal:
            if caixa.cliente_em_atendimento:
                if caixa.cliente_em_atendimento.calcular_tempo_espera() >= 15:
                    self.abrir_caixa("normal")
                else:
                    caixa.atualizar_estado("atendimento_normal")
            else:
                caixa.chamar_proximo_cliente(self.fila_normal, self.fila_preferencial)
        for caixa in self.caixas_preferencial:
            if caixa.cliente_em_atendimento:
                if caixa.cliente_em_atendimento.calcular_tempo_espera() >= 15:
                    self.abrir_caixa("preferencial")
                else:
                    caixa.atualizar_estado("atendimento_preferencial")
            else:
                caixa.chamar_proximo_cliente(self.fila_preferencial, self.fila_normal)
    
    def atender_clientes(self, duracao_minutos):
        duracao_total = 0
        while duracao_total < duracao_minutos:
            self.atualizar_caixas()
            duracao_total += 1
    
    def exibir_estatisticas(self):
        total_clientes_atendidos = len(self.clientes_atendidos)
        total_tempo_espera = sum([cliente.calcular_tempo_espera() for cliente in self.clientes_atendidos])
        if total_clientes_atendidos > 0:
            media_tempo_espera = total_tempo_espera / total_clientes_atendidos
            print(f"Total de clientes atendidos: {total_clientes_atendidos}")
            print(f"Tempo médio de espera: {media_tempo_espera:.2f} minutos")
        else:
            print("Nenhum cliente foi atendido.")


sistema_atendimento = SistemaAtendimento(10, 5)

print(sistema_atendimento.gerar_senha_numerica("normal"))
print(sistema_atendimento.gerar_senha_numerica("normal"))
print(sistema_atendimento.gerar_senha_numerica("preferencial"))
print(sistema_atendimento.gerar_senha_numerica("normal"))
print(sistema_atendimento.gerar_senha_numerica("preferencial"))
print(sistema_atendimento.gerar_senha_numerica("normal"))
print(sistema_atendimento.gerar_senha_numerica("normal"))
print(sistema_atendimento.gerar_senha_numerica("normal"))
print(sistema_atendimento.gerar_senha_numerica("normal"))

sistema_atendimento.abrir_caixa("normal")

sistema_atendimento.atender_clientes(60)

sistema_atendimento.exibir_estatisticas()