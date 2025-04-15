from os.path import split

from flask import Flask, jsonify, request
from sapatones import sapatos

app = Flask(__name__)


@app.route('/sapatos', methods=['GET'])
def listar_sapatos():
    marca = request.args.get('marca')
    modelo = request.args.get('modelo')
    cor = request.args.get('cor')
    tamanho = request.args.get('tamanho')
    valor_min = request.args.get('valor_min')
    valor_max = request.args.get('valor_max')
    preco_asc = request.args.get('preco_asc')
    preco_desc = request.args.get('preco_desc')
    estoque = request.args.get('estoque')
    ordenar_marca = request.args.get('ordenar_marca')

    if ordenar_marca and ordenar_marca.lower() == 'true':
        lista_ordenada =  sorted(sapatos, key=lambda x: x ['marca'].lower())
        return jsonify(lista_ordenada)

    if estoque and estoque.lower() == 'true':
        list_estoque = []
        for sapato in sapatos:
            if sapato['estoque'] >= 1:
                list_estoque.append(sapato)

        return jsonify(list_estoque)

    if preco_asc:
        list_asc = sorted(sapatos, key=lambda x: x['preco'])
        return jsonify(list_asc)

    if preco_desc:
        lista_desc = sorted(sapatos, key=lambda x: x['preco'], reverse=True)
        return jsonify(lista_desc)

    if valor_min and valor_max:
        valor_min = float(valor_min)
        valor_max = float(valor_max)
        lista_valor = []

        for sapato in sapatos:
            if sapato['preco'] <= valor_max and sapato['preco'] >= valor_min:
                lista_valor.append(sapato)

        return jsonify(lista_valor)

    if cor and marca and modelo and tamanho:
        tamanho = float(tamanho)
        lista_filtrades = []
        for sapato in sapatos:
            if sapato['marca'].lower() == marca.lower() and sapato['cor'].lower() == cor.lower() and sapato['modelo'].lower() == modelo.lower() and sapato['tamanho'] == tamanho:
                lista_filtrades.append(sapato)

        return jsonify(lista_filtrades)

    if cor and marca and tamanho:
        tamanho = float(tamanho)
        lista_filtrades = []
        for sapato in sapatos:
            if sapato['marca'].lower() == marca.lower() and sapato['cor'].lower() == cor.lower() and sapato['tamanho'] == tamanho:
                lista_filtrades.append(sapato)

        return jsonify(lista_filtrades)

    if cor and tamanho and modelo:
        tamanho = float(tamanho)
        lista_filtrades = []
        for sapato in sapatos:
            if sapato['tamanho'] == tamanho and sapato['cor'].lower() == cor.lower() and sapato['modelo'].lower() == modelo.lower():
                lista_filtrades.append(sapato)

        return jsonify(lista_filtrades)

    if tamanho and marca and modelo:
        tamanho = float(tamanho)
        lista_filtrades = []
        for sapato in sapatos:
            if sapato['marca'].lower() == marca.lower() and sapato['tamanho'] == tamanho and sapato['modelo'].lower() == modelo.lower():
                lista_filtrades.append(sapato)

        return jsonify(lista_filtrades)

    if cor and marca and modelo:
        lista_filtrades = []
        for sapato in sapatos:
            if sapato['marca'].lower() == marca.lower() and sapato['cor'].lower() == cor.lower() and sapato['modelo'].lower() == modelo.lower():
                lista_filtrades.append(sapato)

        return jsonify(lista_filtrades)

    if tamanho and marca:
        tamanho = float(tamanho)
        lista_filtrada = []

        for sapato in sapatos:
            if sapato['tamanho'] == tamanho and sapato['marca'].lower() == marca.lower():
                lista_filtrada.append(sapato)

        return jsonify(lista_filtrada)

    if cor and modelo:
        lista_filtrada_por_cor_e_marca = []
        for sapato in sapatos:
            if sapato['modelo'].lower() == modelo.lower() and sapato['cor'].lower() == cor.lower():
                lista_filtrada_por_cor_e_marca.append(sapato)

        return jsonify(lista_filtrada_por_cor_e_marca)

    if modelo and marca:
        lista_filtrada_por_cor_e_marca = []
        for sapato in sapatos:
            if sapato['marca'].lower() == marca.lower() and sapato['modelo'].lower() == modelo.lower():
                lista_filtrada_por_cor_e_marca.append(sapato)

        return jsonify(lista_filtrada_por_cor_e_marca)

    if cor and marca:
        lista_filtrada_por_cor_e_marca = []
        for sapato in sapatos:
            if sapato['marca'].lower() == marca.lower() and sapato['cor'].lower() == cor.lower():
                lista_filtrada_por_cor_e_marca.append(sapato)

        return jsonify(lista_filtrada_por_cor_e_marca)

    if tamanho:
        tamanho = float(tamanho)
        lista_tamanhes = []
        for sapato in sapatos:
            if sapato['tamanho'] == tamanho:
                lista_tamanhes.append(sapato)
        return lista_tamanhes

    if marca:
        lista_filtrada_por_marca = []
        for sapato in sapatos:
            if sapato['marca'].lower() == marca.lower():
                lista_filtrada_por_marca.append(sapato)

        return jsonify(lista_filtrada_por_marca)

    if cor:
        cores = [c.strip().lower() for c in cor.split(',')]  # separa e normaliza
        lista_filtrar_por_cor = []
        for sapato in sapatos:
            if sapato['cor'].lower() in cores:
                lista_filtrar_por_cor.append(sapato)

        return jsonify(lista_filtrar_por_cor)

    if modelo:
        lista_filtrar_modelo = []
        for sapato in sapatos:
            if sapato['modelo'].lower() == modelo.lower():
                lista_filtrar_modelo.append(sapato)

        return jsonify(lista_filtrar_modelo)

    return jsonify(sapatos)

@app.route('/sapatos/barato', methods=['GET'])
def lista_bara():
    leng = []
    for sapato in sapatos:
        if sapato['preco'] < 300:
            leng.append(sapato)

    return leng

@app.route('/sapatos/promocao', methods=['GET'])
def lista_promo():

    total = sum([sapato['preco'] for sapato in sapatos ])
    media = total / len(sapatos)
    por = media * 0.8
    leng = []

    for sapato in sapatos:
        if sapato['preco'] < por:
            leng.append(sapato)

    return jsonify(leng)


if __name__ == '__main__':
    app.run(debug=True)
