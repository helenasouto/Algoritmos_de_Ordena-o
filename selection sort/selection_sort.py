import time

def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        dados = arquivo.read().split()  # Lê e separa por espaços/quebras de linha
        return list(map(int, dados))    # Converte para lista de inteiros

def selection_sort(lista):
    tamanho = len(lista)
    for j in range (tamanho-1):
        #não precisa ir até a última posição, o ultimo elemento já é ordenado no processo
        min_index = j
        # Assume que o mínimo é o primeiro elemento não ordenado
        for i in range (j+1, tamanho):
        #não precisa comparar com ele mesmo 
            if lista [i] < lista[min_index]:
        #verifica se o valor é menor que o mínimo
                min_index = i
        #se for, se torna o novo mínimo
        if lista [j] > lista[min_index]:
        #se quem ta na posição no momento é maior do que o mínimo
            var = lista[j]
        #variavel auxiliar pra não perder o valor
            lista[j] = lista[min_index]
        #troca de posição
            lista [min_index] = var

def insertion_sort(lista):
    tamanho = len(lista)
    for i in range (1,tamanho):

        if i % 1000 == 0:  
            print(f"Progresso: {i}/{tamanho} elementos processados...")

        #pegar o elemento na posição atual pra comparar com os da lista menor
        atual = lista[i]
        #basta verificar o que ta esquerda, porque a lista já ta ordenada, não precisa comparar com todos os elementos
        j = i - 1

        while j>= 0 and lista[j]>atual:
            # Enquanto houver elementos maiores que 'atual', desloque-os para a direita
            lista[j + 1]=lista[j]
            #não ficar preso no loop
            j = j - 1
        lista [j+1] = atual
        #insere oatual na posição certa

arquivo_professor = "num.100000.2.in"  # Substitua pelo nome do arquivo do professor

# 1. Lê o arquivo
numeros = ler_arquivo(arquivo_professor)
print(f"Total de números lidos: {len(numeros)}")  # Ex: 1000

# 2. Testa o SelectionSort e mede o tempo
copia_numeros = numeros.copy()  # Para não alterar a lista original
inicio_selection = time.time()
selection_sort(copia_numeros)
tempo_selection = time.time() - inicio_selection
print(f"\nTempo do SelectionSort: {tempo_selection:.5f} segundos")

# 3. Testa o InsertionSorts
copia_insertion = numeros.copy()
inicio_insertion = time.time()
insertion_sort(copia_insertion)
tempo_insertion = time.time() - inicio_insertion
print(f"Tempo do InsertionSort: {tempo_insertion:.5f} segundos")


# 4. Verifica se ordenou corretamente (comparando com o sorted do Python)
if copia_numeros == sorted(numeros):
    print("SelectionSort: Resultado correto!")
else:
    print("SelectionSort: Erro na ordenação!")
if copia_insertion == sorted(numeros):
    print("InsertionSort ordenou corretamente!")
else:
    print("Erro no InsertionSort!")

# 5. Comparação de desempenho
if tempo_selection  < tempo_insertion:
    print("\nSelectionSort foi mais rápido!")
elif tempo_insertion < tempo_selection :
    print("\nInsertionSort foi mais rápido!\n")
else:
    print("\nOs dois algoritmos tiveram o mesmo tempo!")