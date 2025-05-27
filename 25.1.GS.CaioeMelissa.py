quantidade_desastres = []
tipos_desastres = []
paises = []
cidades = []
bairros = []
ruas = []
total_afetados = []
criancas = []
adultos = []
idosos = []
mobilidade_reduzida = []
feridos = []
while True:
    qtd_desastres = int(input("Insira a quantidade de desastres: "))
    quantidade_desastres.append(qtd_desastres)
    for i in range(qtd_desastres):
        tipos_desastres.append(input("Insira o tipo de desastre: "))
        paises.append(input("Insira o país: "))
        cidades.append(input("Insira a cidade: "))
        bairros.append(input("Insira o bairro: "))
        ruas.append(input("Insira a rua: "))
        qtd = int(input("Insira a quantidade de afetados: "))
        total_afetados.append(qtd)
        cri = int(input("Insira a quantidade de crianças afetadas: "))
        criancas.append(cri)
        adu = int(input("Insira a quantidade de adultos afetados: "))
        adultos.append(adu)
        ido = int(input("Insira a quantidade de idosos afetados: "))
        idosos.append(ido)
        mobr = int(input("Insira a quantidade de pessoas com mobilidade reduzida afetadas: "))
        mobilidade_reduzida.append(mobr)
        fer = int(input("Insira a quantidade de feridos: "))
        feridos.append(fer)
        if not (cri + adu + ido + mobr + fer) == qtd:
            print("Por favor, preencha os dados novamente.")
            paises.clear()
            cidades.clear()
            bairros.clear()
            ruas.clear()
            total_afetados.clear()
            criancas.clear()
            adultos.clear()
            idosos.clear()
            mobilidade_reduzida.clear()
            feridos.clear()
            break
        print("Obrigado! Próximo registro!")
    print("Obrigado!")
    print("Gostaria de inserir mais desastres?")
    simounao = input("Sim = S ")
    if simounao != "S":
        break
print("Total de desastres:", sum(quantidade_desastres))
print("Afetados por categoria: | Crianças:", sum(criancas), "| Adultos:", sum(adultos), "| Idosos:", sum(idosos), "| Mobilidade reduzida:", sum(mobilidade_reduzida), "| Feridos:", sum(feridos))
categoria_afetada = max(sum(criancas), sum(adultos), sum(idosos), sum(mobilidade_reduzida), sum(feridos))
categorias = [
    ("Crianças", criancas),
    ("Adultos", adultos),
    ("Idosos", idosos),
    ("Mobilidade reduzida", mobilidade_reduzida),
    ("Feridos", feridos)
]
for nome, lista in categorias:
    if sum(lista) == categoria_afetada:
        cat_af = nome
        break
print("A categoria mais afetada é a:", cat_af)
print("Total de pessoas afetadas:", sum(total_afetados))
maior = max(total_afetados)
pos_maior = total_afetados.index(maior)
print("Local do desastre com maior número de afetados:", ruas[pos_maior], "| Bairro:", bairros[pos_maior], "| Cidade:", cidades[pos_maior], "| País:", paises[pos_maior], "| Tipo:", tipos_desastres[pos_maior])


