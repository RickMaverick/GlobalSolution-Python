#SISTEMA DE DOACAO
#Fazer Doação

def perguntar_doacao(cadastro):
 if cadastro[0] == "DOADOR":
     print(f"Bem vindo, {cadastro[2]}!")
     while True:
         resposta = input("Gostaria de fazer uma doação?")
         if resposta.upper() == "SIM":
             print("Fazendo doação...")
             #doar()

         elif resposta.upper() == "NAO" or resposta.upper() == "NAO":
             print("Tudo bem, fique a vontade para navegar por nosso App!")
             break
         else:
             print("Digite 'Sim' ou 'Não', por favor")

#def doar():