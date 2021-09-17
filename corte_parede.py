def calculaCorte(arrayParede):
    # pegar tamanho da parede
    tamanhoParede = sum(arrayParede[0])
    # criar array novo de intersect com tamanho da parede
    intersect = [0] * tamanhoParede
    # entra em cada array
    for arr in arrayParede:
        #  dentro do array, passar por todos os valores - 1
        soma = 0
        for ele in (arr[0:-1]):
            #  gravar +1 no index do intersect
            soma += ele
            intersect[soma] += 1
    # retornar o index com maior número de intersec
    print(intersect.index(max(intersect)))


if __name__ == "__main__":
    arrayParede = [[3, 5, 1, 1], [2, 3, 3, 2], [5, 5],
                   [4, 4, 2], [1, 3, 3, 3], [1, 1, 6, 1, 1]]
    calculaCorte(arrayParede)
