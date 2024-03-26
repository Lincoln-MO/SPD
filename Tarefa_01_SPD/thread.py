# Importação dos módulos necessários
import threading  # Para trabalhar com threads
import time  # Para medir o tempo de execução
import re  # Para manipulação de expressões regulares

# Função que será executada por cada thread
def worker(params):
    # Desempacotando os parâmetros recebidos
    threadNum, lista = params
    start_time = time.time()  # Tempo inicial

    # Operações realizadas pela thread
    linhas = lista[threadNum]  # Obtendo as linhas correspondentes à thread
    listaString = "".join(linhas)  # Concatenando as linhas em uma única string
    conteudo = listaString.strip()  # Removendo espaços em branco do início e do final da string
    palavras = re.split(r'\s+', conteudo)  # Dividindo a string em palavras utilizando expressão regular

    # Contagem do número de palavras
    numero_de_palavras = len(palavras)
    end_time = time.time()  # Tempo final

# Função para executar as threads
def exec(vetor):
    threads = [] # Inicializando uma lista vazia

    # Criando e iniciando as threads
    for i in range(len(vetor)):
        params = (i, vetor)
        t = threading.Thread(target=worker, args=(params,))
        threads.append(t) # Adicionando o elemento à lista. Util para adicionar elementos dinamicamente a uma lista conforme necessário durante a execução do programa.
        t.start()

    # Ponto de sincronização: aguardando o término de todas as threads
    for i in threads:
        i.join()

# Função para dividir uma lista em partes para processamento paralelo
def divideVetor(lista, n):
    vetorFinal = []
    tamanhoLista = len(lista)
    tamanhoDeCadaPedaco = tamanhoLista // n  #divisão inteira
    elementosExtras = tamanhoLista % n # resto da divisao

    inicio = 0
    for i in range(n):
        if i == n - 1:
            fim = inicio + tamanhoDeCadaPedaco + elementosExtras
        else:
            fim = inicio + tamanhoDeCadaPedaco
        vetorFinal.append(lista[inicio:fim])  # Adicionando uma parte do vetor ao vetor final
        inicio = fim

    return vetorFinal

# Função principal do programa
def main():
    # Abertura do arquivo "hamlet.txt" para leitura, especificando o encoding como UTF-8
    with open("F:\Área de Trabalho\SIstemas paralelos e distribuidos\Tarefa_SPD_01\Tarefa_01_SPD\hamlet.txt", "r", encoding="utf-8") as arquivo:
        # Leitura do conteúdo do arquivo e divisão em linhas
        linhas = arquivo.readlines()

    # Divisão das linhas em partes para processamento paralelo
    vetor = divideVetor(linhas, 2)
    
    # Execução das partes em threads
    exec(vetor)

# Verificação se este script está sendo executado diretamente
if __name__ == "__main__":
    # Chamada da função principal
    main()