

def filtrar_mo(sapatos, modelo):
    if modelo:
        lista_filtrar_modelo = []
        for sapato in sapatos:
            if sapato['modelo'].lower() == modelo.lower():
                lista_filtrar_modelo.append(sapato)

        return lista_filtrar_modelo

def filtrar_cor(cor, sapatos):
    if cor:
        lista_filtrar_por_cor = []
        for sapato in sapatos:
            if sapato['cor'].lower() == cor.lower():
                lista_filtrar_por_cor.append(sapato)

        return lista_filtrar_por_cor

def filtrar_marca(sapatos, marca):
    if marca:
        lista_filtrada_por_marca = []
        for sapato in sapatos:
            if sapato['marca'].lower() == marca.lower():
                lista_filtrada_por_marca.append(sapato)

        return lista_filtrada_por_marca

def filtrar_cor_mar(sapatos, marca, cor):
    if cor and marca:
        lista_filtrada_por_cor_e_marca = []
        for sapato in sapatos:
            if sapato['marca'].lower() == marca.lower() and sapato['cor'].lower() == cor.lower():
                lista_filtrada_por_cor_e_marca.append(sapato)

        return lista_filtrada_por_cor_e_marca

def filtrar_mo_mar(sapatos, marca, modelo):
    if modelo and marca:
        lista_filtrada_por_cor_e_marca = []
        for sapato in sapatos:
            if sapato['marca'].lower() == marca.lower() and sapato['modelo'].lower() == modelo.lower():
                lista_filtrada_por_cor_e_marca.append(sapato)

        return lista_filtrada_por_cor_e_marca

def filtar_cor_mo(sapatos,cor,modelo):
    if cor and modelo:
        lista_filtrada_por_cor_e_marca = []
        for sapato in sapatos:
            if sapato['modelo'].lower() == modelo.lower() and sapato['cor'].lower() == cor.lower():
                lista_filtrada_por_cor_e_marca.append(sapato)

        return lista_filtrada_por_cor_e_marca

def filtrar_cor_mar_mo(sapatos,cor,modelo,marca):
    if cor and marca and modelo:
        lista_filtrades = []
        for sapato in sapatos:
            if sapato['marca'].lower() == marca.lower() and sapato['cor'].lower() == cor.lower() and sapato['modelo'].lower() == modelo.lower():
                lista_filtrades.append(sapato)

        return lista_filtrades

def filtrar_ta_mar_mo(sapatos,marca,tamanho,modelo):
    if tamanho and marca and modelo:
        lista_filtrades = []
        for sapato in sapatos:
            if sapato['marca'].lower() == marca.lower() and sapato['tamanho'] == tamanho and sapato['modelo'].lower() == modelo.lower():
                lista_filtrades.append(sapato)

        return

def filtrar_ta_cor_mar(sapatos,marca,cor,tamanho):
    if cor and marca and tamanho:
        lista_filtrades = []
        for sapato in sapatos:
            if sapato['marca'].lower() == marca.lower() and sapato['cor'].lower() == cor.lower() and sapato['tamanho'] == tamanho:
                lista_filtrades.append(sapato)

        return lista_filtrades

def filtrar_cor_ta_mo(cor,tamanho,modelo,sapatos):
    if cor and tamanho and modelo:
        lista_filtrades = []
        for sapato in sapatos:
            if sapato['tamanho'] == tamanho and sapato['cor'].lower() == cor.lower() and sapato['modelo'].lower() == modelo.lower():
                lista_filtrades.append(sapato)

        return lista_filtrades

def filtrar_cor_marca_modelo_tamanho(sapatos,cor,marca,modelo,tamanho):
    if cor and marca and modelo and tamanho:
        lista_filtrades = []
        for sapato in sapatos:
            if sapato['marca'].lower() == marca.lower() and sapato['cor'].lower() == cor.lower() and sapato['modelo'].lower() == modelo.lower() and sapato['tamanho'] == tamanho:
                lista_filtrades.append(sapato)

        return lista_filtrades