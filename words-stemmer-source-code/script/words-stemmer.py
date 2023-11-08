import nltk
from nltk.stem import PorterStemmer

nltk.download('punkt')

stemmer = PorterStemmer()

nome_arquivo_entrada = './input/in.txt'

nome_arquivo_saida = './output/out.txt'

with open(nome_arquivo_entrada, 'r', encoding='utf-8') as arquivo_entrada:
    palavras_tokenizadas = arquivo_entrada.read().split() 

palavras_stemizadas = [stemmer.stem(palavra) for palavra in palavras_tokenizadas]

with open(nome_arquivo_saida, 'w', encoding='utf-8') as arquivo_saida:
    for palavra_stemizada in palavras_stemizadas:
        arquivo_saida.write(palavra_stemizada + '\n')