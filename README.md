# create-k-fold

separa os dados em k validações cruzadas e separa os dados em treinamento e teste

## requisitos para usar:

    $ pip install -r requirements.txt

## os arquivos devem:
    entrada/
        classe1/
            arquivo1.formato
            arquivo2.formato
            arquivo_n.formato
        classe2/
            arquivo1.formato
            arquivo2.formato
            arquivo_n.formato
        classe_n/
            arquivo1.formato
            arquivo2.formato
            arquivo_n.formato
    saida/

## para usar

    $ python main.py --entrada a --saida c -k 2 --treinamento 0.8 --teste 0.2

## saida
    saida/
        fold1/
            treinamento/
                arquivo1.formato
                arquivo2.formato
                arquivo_n.formato
            teste/
                arquivo1.formato
                arquivo2.formato
                arquivo_n.formato
        fold2/
            treinamento/
                arquivo1.formato
                arquivo2.formato
                arquivo_n.formato
            teste/
                arquivo1.formato
                arquivo2.formato
                arquivo_n.formato
        fold_n/
            treinamento/
                arquivo1.formato
                arquivo2.formato
                arquivo_n.formato
            teste/
                arquivo1.formato
                arquivo2.formato
                arquivo_n.formato