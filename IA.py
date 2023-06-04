#SISTEMA DE CRUZAMENTO DE INFORMAÇÕES DO DOADOR COM BENEFICIÁRIO
##Filtros para selecionar um Beneficiário: Faturamento/Porte da Empresa, Localização, Preferencia de Entidade
import BancoDados

def cruzar_informacoes(cadastro, tipo_beneficiario_doado):
    lista_beneficiarios = BancoDados.gera_lista_beneficiarios() #função para criar um lista com os dados pré cadastrados no banco de dados
    #checando Localização
    for lista_interna in lista_beneficiarios:
        if cadastro[7] in lista_interna:
            if tipo_beneficiario_doado in