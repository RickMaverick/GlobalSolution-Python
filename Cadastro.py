#SISTEMA DE CADASTRO
def cadastrar():
    print("Antes de tudo, informe qual é seu objetivo com nosso Serviço.")
    while True:
        tipo_cadastro = input("Se quiser virar um DOADOR, digite 'Doar'. Agora, se quiser ser um Beneficiário ou Ponto de Coleta, digite 'Receber': ")
        if tipo_cadastro.upper() == "DOAR":
            cadastrar_doador()
        elif tipo_cadastro.upper() == "Receber":
            #cadastrar_beneficiario()
        else:
            print("Não entendi o que escreveu. Poderia re-escrever?")

def cadastrar_doador():
    print("Vamos começar seu cadastro!\n"
          "Precisamos saber se você está se cadastrando como uma Pessoa Física, ou como Pessoa Jurídica.")

    # Cadastro - categoria
    while True:
        categoria = input("Caso seja uma Pessoa Física, digite 'PF', caso seja uma Empresa, digite 'PJ': ")
        if categoria.upper() == "PF":
            print("Certo, então você é uma Pessoa Física.")
            categoria = categoria.upper()
            break
        elif categoria.upper() == "PJ":
            print("Certo, então você é uma Empresa.")
            categoria = categoria.upper()
            break
        else:
            print("Não entendi sua resposta.")

    # Cadastro - Guardando identificadores e senha
    if categoria == "PF":
        cadastro = []
        nome = input("Me informe seu 1º Nome: ")
        sobrenome = input(f"{nome}, qual é seu sobrenome: ")
        cpf = input("Agora me informe seu CPF: ")
        email = input("Seu melhor E-mail, por favor: ")
        senha = input("Por último, digite uma senha: ")
        cadastro.append(categoria)
        cadastro.append(nome)
        cadastro.append(sobrenome)
        cadastro.append(cpf)
        cadastro.append(email)
        cadastro.append(senha)
        print(f"Parabens, {nome}, seu cadastro foi feito com Sucesso!\n"
              "Agora você está um passo a menos de dar seu 1º Match com um beneficiário.")

    elif categoria == "PJ":
        cadastro = []
        nome_empresa = input("Me informe o Nome fantasia da empresa: ")
        cnpj = input("Agora me informe o CNPJ: ")
        email = input("Digite o E-mail que sera usado para login: ")
        senha = input("Por último, digite uma senha: ")
        cadastro.append(categoria)
        cadastro.append(nome_empresa)
        cadastro.append(cnpj)
        cadastro.append(email)
        cadastro.append(senha)
        print(f"O Cadastro de {nome_empresa}, foi feito com Sucesso!\n"
              "Agora você está um passo a menos de dar seu 1º Match com um beneficiário.")

    return cadastro

def cadastrar_beneficiario():
    #em andamento

def verifica_cadastro(cadastro):
    verifica_identificador = input("Digite o CPF ou CNPJ de seu cadastro: ")
    if verifica_identificador in cadastro:
        print("Seu cadastro já está ativo.")
    else:
        print(f"Não encontramos {verifica_identificador} em nossas bases de dados...")
        cadastrar()
