# Word Stemming

This is a Python utility for stemming words in a text file. It uses the Python Natural Language Toolkit (NLTK) library with the Porter Stemmer algorithm to reduce words to their root forms.

### Folder Structure

- The **[Words Stemmize Source Code](./words-stemmer-source-code/)** folder contains the inputs and outputs used in the created project, as well as the source code itself.
- In the **[Script](./words-stemmer-source-code/script/)** folder, you will find the source code for the project.

## How It Works

The utility reads a text file with tokenized words and stems each word, reducing it to its root form. It uses the NLTK library's Porter Stemmer to perform this task.

## How to Use

Follow these steps to stem words in a text file:

1. Clone this repository or download the source code to your local environment.

2. Modify the `nome_arquivo_entrada` variable to specify the path to your input text file containing tokenized words.

3. Modify the `nome_arquivo_saida` variable to specify the path and name of the output file where the stemmed words will be saved.

4. Run the provided Python script (`stem_words.py`). This script will process the input text file, stem the words, and save the stemmed words to the output file.

5. After execution, the stemmed words will be saved in the output file, with each word on a separate line.

## Note

Make sure to customize the `nome_arquivo_entrada` and `nome_arquivo_saida` variables in the provided Python script to specify your input and output file paths.

Enjoy using this utility to stem words in your text data!