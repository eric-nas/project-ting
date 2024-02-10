from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue
import sys


def process(path_file: str, instance: Queue):
    file_read = txt_importer(path_file)
    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_read),
        "linhas_do_arquivo": file_read
    }

    for data in instance.data:
        if data['nome_do_arquivo'] == path_file:
            return print(result, sys.stdout)
    instance.enqueue(result)
    return print(result, sys.stdout)


def remove(instance: Queue):
    if len(instance) == 0:
        return sys.stdout.write('Não há elementos\n')
    file_remove = instance.dequeue()
    mes = f"Arquivo {file_remove['nome_do_arquivo']} removido com sucesso\n"
    return sys.stdout.write(mes)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
