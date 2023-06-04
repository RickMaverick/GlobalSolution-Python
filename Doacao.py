#SISTEMA DE DOACAO
#Fazer Doação
import IA


def realizar_doacao(cadastro):
 if cadastro[0] == "DOADOR":
     print(f"Bem vindo, {cadastro[2]}!")
     while True:
         resposta = input("Gostaria de fazer uma doação?")
         if resposta.upper() == "SIM":
             tipo_beneficiario_doado = preferencias_doacao(cadastro)
             tipo_do_doacao = solicita_tipo_doacao()
             IA.cruzar_informacoes(cadastro)
             doador = cadastro[2]
             resumo_doacao = []
             resumo_doacao.append(doador)
             resumo_doacao.append(tipo_beneficiario_doado)
             resumo_doacao.append(tipo_do_doacao)
             return resumo_doacao
         elif resposta.upper() == "NAO" or resposta.upper() == "NAO":
             print("Tudo bem, fique a vontade para navegar por nosso App!")
             break
         else:
             print("Digite 'Sim' ou 'Não', por favor")


def preferencias_doacao(cadastro):
    #Verificar porte e tipo Doador
    #Doador PJ
    if cadastro[1] == 'PJ':
        if cadastro[8] == "Médio a Grande porte":
            print(f"Como a {cadastro[2]} é uma Empresa de Médio a Grande Porte, você pode doar para tanto para Pontos de Coleta quanto para ONGs de Grande Porte")
            while True:
                print("Digite o código referente ao tipo de Instituição que você quer Doar.")
                doacao_tipo_beneficiario = input("1 - ONGS\n"
                                                 "2 - Pontos de Coleta\n"
                                                 "3 - Outras Instituições")
                if doacao_tipo_beneficiario.isdigit():
                    if int(doacao_tipo_beneficiario) == 1:
                        doacao_tipo_beneficiario = "ONGS"
                        print(f"Perfeito, verificando {doacao_tipo_beneficiario} próximas a sua localização.")
                        return doacao_tipo_beneficiario
                    elif int(doacao_tipo_beneficiario) == 2:
                        doacao_tipo_beneficiario ="Pontos de Coleta"
                        print(f"Perfeito, verificando {doacao_tipo_beneficiario} próximos a sua localização.")
                        return doacao_tipo_beneficiario
                    elif int(doacao_tipo_beneficiario) == 3:
                        doacao_tipo_beneficiario ="Outras Instituições"
                        print(f"Perfeito, verificando {doacao_tipo_beneficiario} próximas a sua localização.")
                        return doacao_tipo_beneficiario
                    else:
                        print("Digite um número dentro das opções.")
                else:
                    print("Digite apenas o número referente a opção desejada.")
        elif cadastro[8] == "Micro e Pequenas Empresas":
            while True:
                print("Digite o código referente ao tipo de Instituição que você quer Doar.")
                doacao_tipo_beneficiario = input("1 - ONGS\n"
                                                 "2 - Pontos de Coleta\n"
                                                 "3 - Outras Instituições")
                if doacao_tipo_beneficiario.isdigit():
                    if int(doacao_tipo_beneficiario) == 1:
                        doacao_tipo_beneficiario = "ONGS"
                        print(f"Perfeito, verificando {doacao_tipo_beneficiario} próximas a sua localização.")
                        return doacao_tipo_beneficiario
                    elif int(doacao_tipo_beneficiario) == 2:
                        doacao_tipo_beneficiario ="Pontos de Coleta"
                        print(f"Perfeito, verificando {doacao_tipo_beneficiario} próximos a sua localização.")
                        return doacao_tipo_beneficiario
                    elif int(doacao_tipo_beneficiario) == 3:
                        doacao_tipo_beneficiario ="Outras Instituições"
                        print(f"Perfeito, verificando {doacao_tipo_beneficiario} próximas a sua localização.")
                        return doacao_tipo_beneficiario
                    else:
                        print("Digite um número dentro das opções.")
                else:
                    print("Digite apenas o número referente a opção desejada.")
    #DOADOR PF
    elif cadastro[1] == "PF":
        while True:
            print("Digite o código referente ao tipo de Instituição que você quer Doar.")
            doacao_tipo_beneficiario = input("1 - ONGS\n"
                                            "2 - Pontos de Coleta\n"
                                            "3 - Outras Instituições")
            if doacao_tipo_beneficiario.isdigit():
                if int(doacao_tipo_beneficiario) == 1:
                    doacao_tipo_beneficiario = "ONGS"
                    print(f"Perfeito, verificando {doacao_tipo_beneficiario} próximas a sua localização.")
                    return doacao_tipo_beneficiario
                elif int(doacao_tipo_beneficiario) == 2:
                    doacao_tipo_beneficiario = "Pontos de Coleta"
                    print(f"Perfeito, verificando {doacao_tipo_beneficiario} próximos a sua localização.")
                    return doacao_tipo_beneficiario
                elif int(doacao_tipo_beneficiario) == 3:
                    doacao_tipo_beneficiario = "Outras Instituições"
                    print(f"Perfeito, verificando {doacao_tipo_beneficiario} próximas a sua localização.")
                    return doacao_tipo_beneficiario
                else:
                    print("Digite um número dentro das opções.")
            else:
                print("Digite apenas o número referente a opção desejada.")


def solicita_tipo_doacao():
    while True:
        print("O alimento a ser doado é percivel?")
        resposta = input("1 - Alimentos Perecíveis (Frutas, Legumes, Hortaliças, Frios, etc)\n"
                         "2 - Alimentos Não Perecíveis (Grãos, Ingredientes Culinários, Sementes, etc)")
        if resposta.isdigit():
            if int(resposta) == 1:
                perecivel = "PERECIVEL"
                break
            elif int(resposta) == 2:
                perecivel = "NÃO PERECIVEL"
                break
            else:
                print("Digite um número dentro das opções.")
        else:
            print("Digite apenas o número referente a opção desejada.")
    while True:
        print("Agora informe o tipo de alimento:")
        resposta = input("1 - Alimentos in natura ou minimamente processados (arroz, feijão,ovos, frutas, legumes, etc)\n"
                         "2 - Ingredientes culinários processados (azeite, açúcar, manteiga,sal,etc)\n"
                         "3 - Processados (pão francês, leite,etc)\n"
                         "4 - Ultra processados (bolos, bolachas,cereais, embutidos,etc)\n"
                         "5 - Cesta Básica")
        if resposta.isdigit():
            if int(resposta) == 1:
                categoria_alimento = "Alimentos in natura ou minimamente processados"
                break
            elif int(resposta) == 2:
                categoria_alimento = "Ingredientes culinários processados"
                break
            elif int(resposta) == 3:
                categoria_alimento = "Processados"
                break
            elif int(resposta) == 4:
                categoria_alimento = "Ultra processados"
                break
            elif int(resposta) == 5:
                categoria_alimento = "Cesta Basica"
                break
            else:
                print("Digite um número dentro das opções.")
        else:
            print("Digite apenas o número referente a opção desejada.")
    return perecivel, categoria_alimento