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
        tipo_cadastro = "DOADOR"
        cadastro = []
        nome = input("Me informe seu 1º Nome: ").title()
        sobrenome = input(f"{nome}, qual é seu sobrenome: ").title()
        cpf = input("Agora me informe seu CPF: ")
        email = input("Seu melhor E-mail, por favor: ")
        telefone = solicita_telefone()
        localizacao = solicita_localizacao()
        senha = input("Por último, digite uma senha: ")
        cadastro.append(tipo_cadastro)
        cadastro.append(categoria)
        cadastro.append(nome)
        cadastro.append(sobrenome)
        cadastro.append(cpf) #identificador CPF índice 4
        cadastro.append(email)
        cadastro.append(telefone)
        cadastro.append(localizacao)
        cadastro.append(senha)
        print(f"Parabens, {nome}, seu cadastro foi feito com Sucesso!\n"
              "Agora você está um passo a menos de dar seu 1º Match com um beneficiário.")

    elif categoria == "PJ":
        tipo_cadastro = "DOADOR"
        cadastro = []
        nome_empresa = input("Me informe o Nome fantasia da empresa: ").title()
        segmento_empresa = input("Seguimento da Empresa: ").title()
        cnpj = input("Agora me informe o CNPJ: ")
        email = input("Digite o E-mail que sera usado para login: ")
        telefone = solicita_telefone()
        localizacao = solicita_localizacao()
        print("Seu cadastro está quase pronto!\n"
            "A próxima pergunta é importante pois é um dos critérios que nosso sistema utiliza para nossas recomendações de Beneficiário.")
        categoria_faturamento = solicita_faturamento(nome_empresa)
        senha = input("Por último, digite uma senha: ")
        cadastro.append(tipo_cadastro)
        cadastro.append(categoria)
        cadastro.append(nome_empresa)
        cadastro.append(segmento_empresa)
        cadastro.append(cnpj) #identificador CNPJ índice 4
        cadastro.append(email)
        cadastro.append(telefone)
        cadastro.append(localizacao)
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
        categoria_beneficiario = input("Digite o código correspondente ao tipo de sua Instituição: ")
        if categoria_beneficiario.isdigit():
            categoria = cadastrar_categoria_beneficiario(categoria_beneficiario)
            break
        else:
            print("Não entendi sua resposta.")


    # Cadastro - Guardando identificadores e senha
    tipo_cadastro = "BENEFICIARIO"
    cadastro = []
    nome_beneficiario = input("Me informe o Nome da Instituição: ").title()
    tipo_beneficiario = seguimenta_tipo_beneficiario(nome_beneficiario)
    email = input("Digite o E-mail que sera usado para login: ")
    telefone = solicita_telefone()
    localizacao = solicita_localizacao()
    print("Seu cadastro está quase pronto!\n"
        "A próxima pergunta é importante pois é um dos critérios que nosso sistema utiliza para a recomendação de um Beneficiário a uma empresa ou pessoa.")
    porte_beneficiario = calcula_porte_beneficiario(nome_beneficiario)
    senha = input("Por último, digite uma senha: ")
    cadastro.append(tipo_cadastro)
    cadastro.append(categoria)
    cadastro.append(nome_beneficiario)
    cadastro.append(email)
    cadastro.append(telefone)
    cadastro.append(localizacao)
    cadastro.append(porte_beneficiario)
    cadastro.append(tipo_beneficiario)
    cadastro.append(senha)
    print(f"O Cadastro de {nome_beneficiario}, foi feito com Sucesso!\n"
        "Agora você está um passo a menos de dar seu 1º Match com um Doador.")

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

def calcula_porte_beneficiario(nome_beneficiario):
    while True:
        print(f"Quantos dependentes o {nome_beneficiario} atende?\n"
              "1 - Menos ou igual a 20 pessoas\n"
              "2 - Entre 20 e 50 pessoas\n"
              "3 - Entre 51 e 200 pessoas\n"
              "4 - Entre 201 e 500 pessoas\n"
              "5 - Entre 501 e 1000 pessoas\n"
              "6 - Mais que 1000 pessoas\n")
        porte_beneficiario = input("Digite o código correspondente: ")
        if porte_beneficiario.isdigit():
            if int(porte_beneficiario) == 1:
                porte_beneficiario = "PEQUENO PORTE"
                return porte_beneficiario
            elif int(porte_beneficiario) == 2:
                porte_beneficiario = "PEQUENO PORTE"
                return porte_beneficiario
            elif int(porte_beneficiario) == 3:
                porte_beneficiario = "MÉDIO PORTE"
                return porte_beneficiario
            elif int(porte_beneficiario) == 4:
                porte_beneficiario = "MÉDIO PORTE"
                return porte_beneficiario
            elif int(porte_beneficiario) == 5:
                porte_beneficiario = "GRANDE PORTE"
                return porte_beneficiario
            elif int(porte_beneficiario) == 6:
                porte_beneficiario = "GRANDE PORTE"
                return porte_beneficiario
            else:
                print("Digite um número dentro das opções")
        else:
            print("Não entendi. Digite apenas o numero correspondente.")

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

def solicita_localizacao():
        while True:
            print("Em qual estado sua Organização está localizada?")
            estado = input("1 - São Paulo\n"
                "2 - Espirito Santo\n"
                "3 - Rio de Janeiro\n"
                "4 - Minas Gerais")
            if estado.isdigit():
                if int(estado) == 1:
                    print("Certo. Agora me informe a cidade:")
                    cidade = input("1 - São Paulo\n"
                          "2 - Guarulhos\n"
                          "3 - Sorocaba\n"
                          "4 - Campinhas\n"
                          "5 - Santo André\n"
                          "6 - São Bernardo do Campo\n"
                          "7 - Outro")
                    if cidade.isdigit():
                        if int(cidade) == 1:
                            cidade = "SÃO PAULO"
                            estado = "SP"
                            return estado, cidade
                        elif int(cidade) == 2:
                            cidade = "GUARULHOS"
                            estado = "SP"
                            return estado, cidade
                        elif int(cidade) == 3:
                            cidade = "SOROCABA"
                            estado = "SP"
                            return estado, cidade
                        elif int(cidade) == 4:
                            cidade = "CAMPINAS"
                            estado = "SP"
                            return estado, cidade
                        elif int(cidade) == 5:
                            cidade = "SANTO ANDRÉ"
                            estado = "SP"
                            return estado, cidade
                        elif int(cidade) == 6:
                            cidade = "SÃO BERNARDO DO CAMPO"
                            estado = "SP"
                            return estado, cidade
                        elif int(cidade) == 7:
                            cidade = input("Digite o nome da cidade: ")
                            estado = "SP"
                            return estado, cidade
                        else:
                            print("Esse número não corresponde a nenhum local")
                if int(estado) == 2:
                    print("Certo. Agora me informe a cidade:")
                    cidade = input("1 - Vitória\n"
                          "2 - Linhares\n"
                          "3 - Aracruz\n"
                          "4 - Vila Velha\n"
                          "5 - Outro")
                    if cidade.isdigit():
                        if int(cidade) == 1:
                            cidade = "VITÓRIA"
                            estado = "ES"
                            return estado, cidade
                        elif int(cidade) == 2:
                            cidade = "LINHARES"
                            estado = "ES"
                            return estado, cidade
                        elif int(cidade) == 3:
                            cidade = "ARACRUZ"
                            estado = "ES"
                            return estado, cidade
                        elif int(cidade) == 4:
                            cidade = "VILA VELHA"
                            estado = "ES"
                            return estado, cidade
                        elif int(cidade) == 5:
                            cidade = input("Digite o nome da cidade: ")
                            estado = "ES"
                            return estado, cidade
                        else:
                            print("Esse número não corresponde a nenhum local")
                if int(estado) == 3:
                    print("Certo. Agora me informe a cidade:")
                    cidade = input("1 - Rio de Janeiro\n"
                          "2 - São Gonçalo\n"
                          "3 - Duque de Caxias\n"
                          "4 - Nova Iguaçu\n"
                          "5 - Outro")
                    if cidade.isdigit():
                        if int(cidade) == 1:
                            cidade = "RIO DE JANEIRO"
                            estado = "RJ"
                            return estado, cidade
                        elif int(cidade) == 2:
                            cidade = "SÃO GONCALO"
                            estado = "RJ"
                            return estado, cidade
                        elif int(cidade) == 3:
                            cidade = "DUQUE DE CAXIAS"
                            estado = "RJ"
                            return estado, cidade
                        elif int(cidade) == 4:
                            cidade = "NOVA IGUACU"
                            estado = "RJ"
                            return estado, cidade
                        elif int(cidade) == 2:
                            cidade = input("Digite o nome da cidade: ")
                            estado = "RJ"
                            return estado, cidade
                        else:
                            print("Esse número não corresponde a nenhum local")
                if int(estado) == 4:
                    print("Certo. Agora me informe a cidade:")
                    cidade = input("1 - Uberlândia\n"
                          "2 - Belo Horizonte\n"
                          "3 - Juiz de Fora\n"
                          "4 - Montes Claros\n"
                          "5 - Outro")
                    if cidade.isdigit():
                        if int(cidade) == 1:
                            cidade = "UBERLANDIA"
                            estado = "MG"
                            return estado, cidade
                        elif int(cidade) == 2:
                            cidade = "BELO HORIZONTE"
                            estado = "MG"
                            return estado, cidade
                        elif int(cidade) == 3:
                            cidade = "JUIZ DE FORA"
                            estado = "MG"
                            return estado, cidade
                        elif int(cidade) == 4:
                            cidade = "MONTES CLAROS"
                            estado = "MG"
                            return estado, cidade
                        elif int(cidade) == 5:
                            cidade = input("Digite o nome da cidade: ")
                            estado = "MG"
                            return estado, cidade
                        else:
                            print("Esse número não corresponde a nenhuma cidade")
                else:print("Esse número não corresponde a nenhum estado")
            else:
                print("Digite apenas números")

def cadastrar_categoria_beneficiario(categoria_beneficiario):
    if int(categoria_beneficiario) == 1:
        categoria = "ONG"
        print(f"Uma {categoria}? Que legal!")
        return categoria
    elif int(categoria_beneficiario) == 2:
        categoria = "Escola Pública"
        print(f"Uma {categoria}, que bom!")
        return categoria
    elif int(categoria_beneficiario) == 3:
        categoria = "Orfanato"
        print(f"{categoria} né, anotado!")
        return categoria
    elif int(categoria_beneficiario) == 4:
        categoria = "Asilo"
        print(f"Um {categoria} é sempre bem vindo!")
        return categoria
    elif int(categoria_beneficiario) == 5:
        categoria = "Projeto Social"
        print(f"Um {categoria} é sempre bem vindo!")
        return categoria
    elif int(categoria_beneficiario) == 6:
        categoria = input("Digite o tipo de sua Instituição: ")
        return categoria
    else:
        print("Não Entendi.")
        while True:
            categoria = input("1 - ONG\n"
            "2 - Escola Pública\n"
            "3 - Orfanato\n"
            "4 - Asilo\n"
            "5 - Projeto Social Local\n"
            "6 - Outros\n"
            "Digite o código correspondente ao tipo de sua Instituição: ")
            if categoria.isdigit():
                cadastrar_categoria_beneficiario(categoria)
                break
            else:
                print("Não entendi sua resposta.")

def seguimenta_tipo_beneficiario(nome_beneficiario):
    print("Qual frase você mais identifica que contempla a finalidade das doações a sua Instituição?")
    while True:
        resposta = input(f"1 - 'Atuamos como um Ponto de Coleta. As pessoas que ajudamos vão até {nome_beneficiario}, para pegar mantimentos ou se alimentar' Exemplos: Projetos sociais locais, Escolas Públicas\n"
              f"2 - '{nome_beneficiario} utilizara das doações recebidas para abastecimento interno (cozinha, refeitório) e uso próprio de nossos membros. Exemplos: Asilos, Orfanatos, Albergues, Escolas Públicas'\n"
              f"3 - 'As doações serão destinadas/levadas ao grupo de pessoas que a {nome_beneficiario} auxilia. Sendo que a {nome_beneficiario} atua como um intermediário entre as doações e o Grupo de Pessoas em vulnerabilidade que auxiliam. Exemplos: ONGs, Projetos Sociais Maiores'")
        if resposta.isdigit():
            if int(resposta) == 1:
                print("Frase escolhida nº1")
                tipo_beneficiario = "Ponto de Coleta"
                return tipo_beneficiario
            elif int(resposta) == 2:
                print("Frase escolhida nº2")
                tipo_beneficiario = "Beneficiario Proprio"
                return tipo_beneficiario
            elif int(resposta) == 3:
                print("Frase escolhida nº3")
                tipo_beneficiario = "Beneficiario Intermediario"
                return tipo_beneficiario
            else:
                print("Número inválido. Digite um número correspondente aos apresentados.")
        else:
            print("Responda apenas com um dos números referentes a frase escolhida.")