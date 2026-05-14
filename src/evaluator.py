import tiktoken



def contar_tokens(texto):

    encoder = tiktoken.get_encoding("cl100k_base")

    return len(encoder.encode(texto))



def medir_acuracia(resposta, esperado):

    resposta = str(resposta).lower()
    esperado = str(esperado).lower()

    return int(esperado in resposta)

def medir_consistencia(lista_respostas):

    iguais = max(
        lista_respostas.count(x)
        for x in lista_respostas
    )

    return iguais / len(lista_respostas)