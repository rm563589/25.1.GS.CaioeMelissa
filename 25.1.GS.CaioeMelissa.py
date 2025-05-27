tipo_desastre = []
pais = []
cidade = []
bairro = []
rua = []
qtd_total = []
criancas = []
adultos = []
idosos = []
mob_reduzida = []
feridos = []
while True:
    qtd_desastre = int(input("Insira a quantidade de desastres: "))
    for i in range(qtd_desastre):
        tipo_desastre.append(input("Insira o tipo de desastre: "))
        pais.append(input("Insira o país: "))
        cidade.append(input("Insira a cidade: "))
        bairro.append(input("Insira o bairro: "))
        rua.append(input("Insira a rua: "))
        qtd = int(input("Insira a quantidade de afetados: "))
        qtd_total.append(qtd)
        cri = int(input("Insira a quantidade de crianças afetadas: "))
        criancas.append(cri)
        adu = int(input("Insira a quantidade de adultos afetados: "))
        adultos.append(adu)
        ido = int(input("Insira a quantidade de idosos afetados: "))
        idosos.append(ido)
        mobr = int(input("Insira a quantidade de pessoas com mobilidade reduzida afetadas: "))
        mob_reduzida.append(mobr)
        fer = int(input("Insira a quantidade de feridos: "))
        feridos.append(fer)
        if not (cri + adu + ido + mobr + fer) == qtd:
            print("Por favor, preencha os dados novamente.")
            pais.clear()
            cidade.clear()
            bairro.clear()
            rua.clear()
            qtd_total.clear()
            criancas.clear()
            adultos.clear()
            idosos.clear()
            mob_reduzida.clear()
            feridos.clear()
            break
    print("Obrigado!")
    print("Gostaria de inserir mais desastres?")
    simounao = input("Sim = S")
    if simounao != "S":
        break



