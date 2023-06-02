import Doacao
import Cadastro as cd
import Tickets as tk

print("Bem vindo ao FoodBridge! Junte-se a nós e vamos quebrar as barreiras contra a fome.")

while True:
      possui_cadastro = input("Você já possui cadastro? ")
      if possui_cadastro.upper() == "SIM":
            possui_cadastro = 1
            cadastro = []
            break
      elif possui_cadastro.upper() == "NÃO" or possui_cadastro.upper() == "NAO":
            possui_cadastro = 0
            cadastro = []
            break
      else:
            print("Não entendi. Responda de novo, com 'Sim' ou 'Não'.")

#Cadastrando Usuário
if possui_cadastro == 0:
      cadastro = cd.cadastrar()

elif possui_cadastro == 1:
      cadastro = cd.verifica_cadastro(cadastro)

#Ticket confirmando dados do cadastro
ticket_cadastro = tk.gera_ticket_cadastro(cadastro)

#Fazer Doação
Doacao.perguntar_doacao(cadastro)