import nltk
from nltk.stem import PorterStemmer

nltk.download('punkt')

stemmer = PorterStemmer()

def stemmize_words(texto):
    palavras_tokenizadas = texto.split()
    palavras_stemizadas = [stemmer.stem(palavra) for palavra in palavras_tokenizadas]
    return palavras_stemizadas

def stemmize_words_in_file(input_path, output_path):
    try:
        with open(input_path, 'r', encoding='utf-8') as input_file:
            texto = input_file.read()

        palavras_stemizadas = stemmize_words(texto)

        with open(output_path, 'w', encoding='utf-8') as output_file:
            for palavra_stemizada in palavras_stemizadas:
                output_file.write(palavra_stemizada + '\n')

        print(f"Palavras stemizadas e texto salvo em {output_path}")

    except FileNotFoundError:
        print(f"Arquivo {input_path} não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

input_path = './input/in.txt'
output_path = './output/out.txt'

stemmize_words_in_file(input_path, output_path)
