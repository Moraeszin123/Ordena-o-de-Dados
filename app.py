# Algoritmo 1: Bubble Sort (Crescente)
def bubble_sort(arr):  # Função do bubble sort
    n = len(arr)  # Verifica tamanho do vetor
    # Imprime o vetor inicial
    print(f"\nBubble Sort (crescente) - vetor inicial: {arr}")
    for i in range(n-1):  # percorre o vetor
        for j in range(n-1-i):  # compara os elementos adjacentes
            if arr[j] > arr[j+1]:  # verifica se o elemento atual é maior que o próximo
                print(f"Troca: {arr[j]} ↔ {arr[j+1]}")  # imprime a troca
                arr[j], arr[j+1] = arr[j+1], arr[j]  # realiza a troca
                print("Estado do vetor:", arr)  # imprime o vetor pós troca
    print("Resultado final:", arr)  # Imprime o vetor ordenado


# Algoritmo 2: Insertion Sort (Decrescente)
def insertion_sort(arr):  # Função do insertion sort
    # Imprime o vetor inicial
    print(f"\nInsertion Sort (decrescente) - vetor inicial: {arr}")
    for i in range(1, len(arr)):  # Percorre o vetor a partir do segundo elemento
        chave = arr[i]  # Define a chave como o elemento atual
        j = i - 1  # Define j como o índice anterior
        # Compara a chave com os elementos anteriores
        while j >= 0 and arr[j] < chave:
            print(f"Movendo {arr[j]} para a direita")  # Imprime o movimento
            arr[j+1] = arr[j]  # Move o elemento para a direita
            j -= 1  # Decrementa j
            print("Estado do vetor:", arr)  # Imprime o vetor após o movimento
        arr[j+1] = chave  # Insere a chave na posição correta
        # Imprime o vetor após a inserção da chave
        print(f"Inserção da chave {chave}: {arr}")
    print("Resultado final:", arr)  # Imprime o vetor ordenado


# Testes com os três vetores
melhor = [1, 10, 13, 14, 29, 37]  # Vetor em ordem crescente
medio = [29, 10, 14, 37, 13, 1]  # Vetor em ordem aleatória
pior = [37, 29, 14, 13, 10, 1]  # Vetor em ordem decrescente

for vetor in [melhor, medio, pior]:  # chama o bubble sort para cada vetor
    bubble_sort(vetor.copy())

for vetor in [melhor, medio, pior]:  # chama o insertion sort para cada vetor
    insertion_sort(vetor.copy())
