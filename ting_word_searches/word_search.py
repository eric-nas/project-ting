from ting_file_management.queue import Queue


def exists_word(word, instance: Queue):
    result = []
    for archive in instance.data:
        linhas = archive['linhas_do_arquivo']
        for indice, linha in enumerate(linhas, start=1):
            if word in linha.lower():
                result.append({"linha": indice})
        if result == []:
            return result
        return [{
            "palavra": word,
            "arquivo": archive['nome_do_arquivo'],
            "ocorrencias": result
        }]


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
