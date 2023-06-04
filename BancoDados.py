#SIMULAÇÃO DE BANCO DE DADOS : CADASTROS PRÉVIOS

cadastro_ong_grande_1 = ["BENEFICIARIO", "ONG", "Amigos Do Bem", "ricardovtemple@adb.com.br", 11964025807, ('SP', 'SÃO PAULO'), "GRANDE PORTE", "Beneficiario Intermediario", "AmigoDoBem333"]

cadastro_ong_grande_2 = ["BENEFICIARIO", "ONG", "Crianças Contra a Fome", "exemplo@exe.com.br", 11964086808, ('SP', 'SÃO PAULO'), "GRANDE PORTE", "Beneficiario Intermediario", "senhaExemplo@01"]

cadastro_ong_menor_1 = ["BENEFICIARIO", "ONG", "Panetone Transforma", "exemplo@exe.com.br", 11964025809, ('SP', 'SÃO PAULO'), "MÉDIO PORTE", "Beneficiario Intermediario", "senhaExemplo@02"]

cadastro_ong_menor_2 = ["BENEFICIARIO", "ONG", "Sonhar Acordado Campinas", "exemplo@exe.com.br", 11964025810, ('SP', 'CAMPINAS'), "PEQUENO PORTE", "Beneficiario Intermediario", "senhaExemplo@03"]

cadastro_orfanato_1 = ["BENEFICIARIO", "Orfanato", "Familia Acolhedora", "exemplo@exe.com.br", 11964025811, ('SP', 'SÃO PAULO'), "PEQUENO PORTE", "Beneficiario Intermediario", "senhaExemplo@04"]

cadastro_orfanato_2 = ["BENEFICIARIO", "Orfanato", "CantinhoMeimei", "exemplo@exe.com.br", 11964025812, ('RJ', 'RIO DE JANEIRO'), "PEQUENO PORTE", "Beneficiario Intermediario", "senhaExemplo@05"]

cadastro_escola_publica_1 = ["BENEFICIARIO", "Escola Pública", "ETEC José Rocha Mendes", "exemplo@exe.com.br", 11964025813, ('MG', 'UBERLANDIA'), "MÉDIO PORTE", "Beneficiario Intermediario", "senhaExemplo@06"]

cadastro_escola_publica_2 = ["BENEFICIARIO", "Escola Pública", "Colégio Nossa Senhora Aparecida", "exemplo@exe.com.br", 11964025814, ('SP', 'SOROCABA'), "MÉDIO PORTE", "Beneficiario Intermediario", "senhaExemplo@07"]

cadastro_asilo = ["BENEFICIARIO", "Asilo", "Residencial Sênior", "exemplo@exe.com.br", 11964025815, ('ES', 'VITÓRIA'), "PEQUENO PORTE", "Beneficiario Intermediario", "senhaExemplo@08"]

cadastro_projeto_social = ["BENEFICIARIO", "Projeto Social Local", "Construir para Sonhar", "exemplo@exe.com.br", 11964025816, ('SP', 'SÃO PAULO'), "GRANDE PORTE", "Beneficiario Intermediario", "senhaExemplo@09"]

cadastro_projeto_ambiental = ["BENEFICIARIO", "Projeto Ambiental", "GreePeace", "exemplo@exe.com.br", 11964025817, ('SP', 'SÃO PAULO'), "GRANDE PORTE", "Beneficiario Intermediario", "senhaExemplo@10"]

def gera_lista_beneficiarios():
    lista_beneficiarios = [cadastro_ong_grande_1, cadastro_ong_grande_2, cadastro_ong_menor_1, cadastro_ong_menor_2]
    return lista_beneficiarios