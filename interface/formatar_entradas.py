def formatar_nome(nome):
    partes = nome.split()
    partes_formatadas = [parte.capitalize() for parte in partes]
    return ' '.join(partes_formatadas)

def formatar_cpf(cpf):
    cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    return cpf_formatado

def formatar_data_nascimento(data):
    partes = data.split('/')
    data_formatada = f"{partes[0]:02}/{partes[1]:02}/{partes[2]}"
    return data_formatada

def formatar_telefone(telefone):
    telefone_formatado = f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
    return telefone_formatado

def formatar_placa_carro(placa):
    placa_formatada = placa.upper()  # Garante que a placa esteja em maiúsculas
    return placa_formatada
