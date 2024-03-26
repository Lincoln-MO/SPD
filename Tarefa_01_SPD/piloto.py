
# Importação dos módulos necessários
import time  # Para medir o tempo de execução
import subprocess  # Para executar programas externos
import openpyxl  # Para trabalhar com planilhas do Excel

# Função para medir o tempo de execução de um programa
def calculaTempo(programa, nExecucoes):
    i = 2  # Inicialização do índice da célula da planilha

    # Carregar o arquivo Excel que servirá como base de dados
    wb = openpyxl.load_workbook('BaseDeDados.xlsx')

    # Selecionar a planilha ativa
    sheet = wb.active

    # Verificar se é para realizar apenas uma execução do programa
    if nExecucoes == 1:
        # Iniciar a contagem do tempo
        inicio = time.time()
        # Executar o programa uma vez
        subprocess.run(["python", programa], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # Finalizar a contagem do tempo
        fim = time.time()
        # Calcular o tempo de execução
        tempo_execucao = fim - inicio
        # Retornar o tempo de execução
        return tempo_execucao
    else:
        # Se for para realizar múltiplas execuções do programa
        tempos = []  # Lista para armazenar os tempos de execução de cada execução
        # Loop para realizar as execuções
        for _ in range(nExecucoes):
            # Iniciar a contagem do tempo
            inicio = time.time()
            # Executar o programa principal usando subprocess.run
            # Parâmetros:
            #   - ["python", programa]: Lista que representa o comando a ser executado, onde "python" é o interpretador Python 
            #     e "programa" é o nome do programa principal que será passado como argumento para o interpretador Python.
            #   - stdout=subprocess.PIPE: Redireciona a saída padrão (stdout) do processo filho para um pipe, 
            #     permitindo que o processo pai (este script) acesse ou ignore a saída, conforme necessário.
            #   - stderr=subprocess.PIPE: Redireciona a saída de erro padrão (stderr) do processo filho para um pipe, 
            #     permitindo que o processo pai (este script) acesse ou ignore a saída de erro, conforme necessário.
            # Isso garante que qualquer saída gerada pelo programa principal será capturada e pode ser tratada neste script, 
            # sem interferir na saída deste script no console.
            subprocess.run(["python", programa], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            # Finalizar a contagem do tempo
            fim = time.time()
            # Calcular o tempo de execução
            if(programa == "sequencial.py"):
                celula = "A" + str(i)
            elif(programa == "thread.py"):
                celula = "B" + str(i)
            tempo_execucao = fim - inicio
            # Preencher a célula correspondente com o tempo de execução na planilha
            sheet[celula] = tempo_execucao
            i += 1
            # Adicionar o tempo de execução à lista
            tempos.append(tempo_execucao)

        # Calcular a média dos tempos de execução
        media_tempo = sum(tempos) / nExecucoes
        # Determinar a célula onde a média será registrada na planilha
        if(programa == "sequencial.py"):
            celula = "A" + str(i)
        elif(programa == "thread.py"):
            celula = "B" + str(i)
        # Preencher a célula com a média dos tempos de execução
        sheet[celula] = "Media = " + str(media_tempo)
        
        # Salvar as modificações na planilha
        wb.save('BaseDeDados.xlsx')

        # Retornar a média dos tempos de execução
        return media_tempo


def main():
    # Definição dos programas a serem executados e do número de execuções
    programa = "thread.py"
    programa2 = "sequencial.py"
    n_execucoes= 30
   
    # Tempo de execução sequencial
    tempo_sequencial = calculaTempo(programa2, n_execucoes)
    
    # Tempo de execução paralelo
    tempo_paralelo = calculaTempo(programa, n_execucoes)

    # Calculando o speedup
    speedup = tempo_sequencial / tempo_paralelo

    # Exibir os resultados
    print(f"Tempo de execucao sequencial: {tempo_sequencial:.6f} segundos")
    print(f"Tempo de execucao paralelo: {tempo_paralelo:.6f} segundos")
    print(f"Speedup: {speedup:.6f}")

# Verificação se este script está sendo executado diretamente
if __name__ == "__main__":
    # Chamada da função principal
    main()

