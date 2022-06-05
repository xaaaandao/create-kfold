#!/usr/bin/env python
# coding: utf-8

import click
import numpy
from sklearn.model_selection import StratifiedShuffleSplit
from pathlib import Path
import shutil
import os


@click.command()
@click.option(
    '--entrada',
    '-e',
    required=True
)
@click.option(
    '--saida',
    '-s',
    required=True,
)
@click.option(
    '-k',
    required=True,
    help='Numero de folds',
    type=int
)
@click.option(
    '--treinamento',
    required=True,
    help='Porcentagem de dados para treinamento',
    type=float
)
@click.option(
    '--teste',
    required=True,
    help='Porcentagem de dados para teste',
    type=float
)
def main(entrada, saida, k, treinamento, teste):
    print(f'entrada {entrada}')
    print(f'saida {saida}')
    print(f'k {k}')
    print(f'treinamento {treinamento}')
    print(f'teste {teste}')

    if not os.path.isdir(entrada) or not os.path.isdir(saida):
        raise RuntimeError(f'Diretorio nao encontrado')

    X = numpy.array([arquivo.absolute().as_posix() for arquivo in sorted(Path(entrada).rglob('*.*'))])
    todas_classes = [diretorio.absolute().as_posix() for diretorio in Path(entrada).glob('*')]

    y = numpy.array([])
    for arquivo in X:
        y = numpy.append(y, numpy.array([todas_classes.index(classe) for classe in todas_classes if classe in str(arquivo)]))

    for i, (indice_treinamento, indice_teste) in enumerate(StratifiedShuffleSplit(n_splits=k, train_size=treinamento, test_size=teste).split(X, y)):
        if not os.path.isdir(os.path.join(saida, f'fold{i}/treinamento')) or not os.path.isdir(os.path.join(saida, f'fold{i}/teste')):
            os.makedirs(os.path.join(saida, f'fold{i}/treinamento'))
            os.makedirs(os.path.join(saida, f'fold{i}/teste'))

        arquivo_info = open(os.path.join(saida, f'fold{i}/info.md'), 'w')
        arquivo_info.write('acuracia: \n')
        arquivo_info.write(f'\n|arquivos treinamento ({len(indice_treinamento)})|\n')
        arquivo_info.write('|--------------------|\n')

        for arquivo_treinamento in X[indice_treinamento]:
            shutil.copy(arquivo_treinamento, os.path.join(saida, f'fold{i}/treinamento'))
            arquivo_info.write(f'|{arquivo_treinamento}|\n')

        arquivo_info.write(f'\n|arquivos teste ({len(indice_teste)})|\n')
        arquivo_info.write('|--------------------|\n')
        for arquivo_teste in X[indice_teste]:
            shutil.copy(arquivo_teste, os.path.join(saida, f'fold{i}/teste'))
            arquivo_info.write(f'|{arquivo_teste}|\n')


if __name__ == "__main__":
    main()