import sys
import os


def txt_importer(path_file):
    if path_file.find('.txt') < 0:
        return print('Formato inválido', file=sys.stderr)
    if os.path.exists(path_file):
        with open(path_file, "r") as file:
            content = file.readlines()
            content_sem_quebras = [linha.strip() for linha in content]
            return content_sem_quebras
    else:
        return print(f'Arquivo {path_file} não encontrado', file=sys.stderr)
