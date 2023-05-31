#SISTEMA DE CADASTRO
def cadastrar():
    print("Antes de tudo, informe qual é seu objetivo com nosso Serviço.")
    while True:
        tipo_cadastro = input("Se quiser virar um DOADOR, digite 'Doar'. Agora, se quiser ser um Beneficiário, digite 'Receber': ")
        if tipo_cadastro.upper() == "DOAR":
            return cadastrar_doador()
        elif tipo_cadastro.upper() == "RECEBER":
            return cadastrar_beneficiario()
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
        telefone = solicita_telefone()
        senha = input("Por último, digite uma senha: ")
        cadastro.append(categoria)
        cadastro.append(nome)
        cadastro.append(sobrenome)
        cadastro.append(cpf) #identificador CPF índice 3
        cadastro.append(email)
        cadastro.append(telefone)
        cadastro.append(senha)
        print(f"Parabens, {nome}, seu cadastro foi feito com Sucesso!\n"
              "Agora você está um passo a menos de dar seu 1º Match com um beneficiário.")

    elif categoria == "PJ":
        cadastro = []
        nome_empresa = input("Me informe o Nome fantasia da empresa: ")
        segmento_empresa = input("Seguimento da Empresa: ")
        cnpj = input("Agora me informe o CNPJ: ")
        email = input("Digite o E-mail que sera usado para login: ")
        telefone = solicita_telefone()
        print("Legal, seu cadastro está quase pronto!\n"
            "A próxima pergunta é importante pois é um dos critérios que nosso sistema utiliza para nossas recomendações de Beneficiário.")
        categoria_faturamento = solicita_faturamento(nome_empresa)
        senha = input("Por último, digite uma senha: ")
        cadastro.append(categoria)
        cadastro.append(nome_empresa)
        cadastro.append(segmento_empresa)
        cadastro.append(cnpj) #identificador CPF índice 3
        cadastro.append(email)
        cadastro.append(telefone)
        cadastro.append(categoria_faturamento)
        cadastro.append(senha)
        print(f"O Cadastro de {nome_empresa}, foi feito com Sucesso!\n"
              "Agora você está um passo a menos de dar seu 1º Match com um beneficiário.")

    return cadastro

def cadastrar_beneficiario():
    print("Show! Ficamos muito felizes em ver mais um beneficiário entrando no time Food Bridge!\n"
          "Antes de tudo, precisamos entender que tipo de Beneficiário você é!")
    print()
    print("1 - ONG\n"
          "2 - Escola Pública\n"
          "3 - Orfanato\n"
          "4 - Asilo\n"
          "5 - Projeto Social Local\n"
          "6 - Outros")

    # Cadastro - categoria
    while True:
        categoria = input("Digite o código correspondente ao tipo de sua Instituição: ")
        if categoria.isdigit():
            cadastrar_beneficiario_categoria(categoria)
            break
        else:
            print("Não entendi sua resposta.")

    # Cadastro - Guardando identificadores e senha
    cadastro = []
    nome_empresa = input("Me informe o Nome : ")
    segmento_empresa = input("Seguimento da Empresa: ")
    cnpj = input("Agora me informe o CNPJ: ")
    email = input("Digite o E-mail que sera usado para login: ")
    telefone = solicita_telefone()
    print("Legal, seu cadastro está quase pronto!\n"
        "A próxima pergunta é importante pois é um dos critérios que nosso sistema utiliza para nossas recomendações de Beneficiário.")
    categoria_faturamento = solicita_faturamento(nome_empresa)
    senha = input("Por último, digite uma senha: ")
    cadastro.append(categoria)
    cadastro.append(nome_empresa)
    cadastro.append(segmento_empresa)
    cadastro.append(cnpj) #identificador CPF índice 3
    cadastro.append(email)
    cadastro.append(telefone)
    cadastro.append(categoria_faturamento)
    cadastro.append(senha)
    print(f"O Cadastro de {nome_empresa}, foi feito com Sucesso!\n"
        "Agora você está um passo a menos de dar seu 1º Match com um beneficiário.")

    return cadastro

def verifica_cadastro(cadastro):
    verifica_identificador = input("Digite o CPF ou CNPJ de seu cadastro: ")
    if verifica_identificador in cadastro:
        print("Seu cadastro já está ativo.")
    else:
        print(f"Não encontramos {verifica_identificador} em nossas bases de dados...\n"
              f"Iremos iniciar um novo cadastro!")
        return cadastrar()

def solicita_faturamento(nome_empresa):
    while True:
        categoria_faturamento = (input(
            f"Digite 1 para Microempresas e Pequenas Empresas (Faturamento anual MENOR OU IGUAL a R$4,8 milhões)\n"
            f"Digite 2 para Empresas de Médio a Grande Porte (Faturamento anual MAIOR QUE R$4,8 milhões)\n"
            f"Qual é o faturamento anual de {nome_empresa}: "))
        if categoria_faturamento == '1':
            categoria_faturamento = "Micro e Pequenas Empresas"
            break
        elif categoria_faturamento == '2':
            categoria_faturamento = "Médio a Grande porte"
            break
        else:
            print("Não entendi...")

    return categoria_faturamento

def solicita_telefone():
    while True:
        telefone = input("Informe seu melhor número para contato (com DDD regional): ")
        if telefone.isdigit():
            if 11 <= len(telefone) < 13:
                int(telefone)
                return telefone
            elif len(telefone) < 11:
                print("Telefone inválido, muito curto.")
            elif len(telefone) > 12:
                print("Telefone inválido, muito longo.")
        else:
            print("Digite apenas números.")

def cadastrar_beneficiario_categoria(categoria):
    if categoria == 1:
        categoria = "ONG"
        print(f"Uma {categoria}? Que legal!")
    elif categoria == 2:
        categoria = "Escola Pública"
        print(f"Uma {categoria}, que bom!")
    elif categoria == 3:
        categoria = "Orfanato"
        print(f"{categoria} né, anotado!")
    elif categoria == 4:
        categoria = "Asilo"
        print(f"Um {categoria} é sempre bem vindo!")
    elif categoria == 5:
        categoria = "Projeto Social"
        print(f"Um {categoria} é sempre bem vindo!")
    return categoria