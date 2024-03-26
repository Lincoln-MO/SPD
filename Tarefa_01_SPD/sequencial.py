# Importação do módulo 're' para lidar com expressões regulares
import re

# Definição da função principal do programa
def main():
    # Abertura do arquivo "hamlet.txt" para leitura, especificando o encoding como UTF-8
    with open("Atividade Avaliativa 1/hamlet.txt", "r", encoding="utf-8") as arquivo:
        # Leitura do conteúdo do arquivo e divisão em linhas
        linhas = arquivo.readlines()
        # Concatenação das linhas em uma única string
        listaString = "".join(linhas)
        # Remoção de espaços em branco do início e do final da string
        conteudo = listaString.strip()
        # Divisão do conteúdo em palavras utilizando expressão regular para encontrar espaços em branco (\s : corresponde a qualquer caractere de espaço em branco em Python, incluindo espaço, tabulação (\t), quebra de linha (\n), retorno de carro (\r), entre outros.  )
        palavras = re.split(r'\s+', conteudo)

        # Contagem do número de palavras
        numero_de_palavras = len(palavras)

    # Exibição do resultado da contagem de palavras
    print("O arquivo tem", numero_de_palavras, "palavras.")

# Verificação se este script está sendo executado diretamente
if __name__ == "__main__":
    # Chamada da função principal
    main()
