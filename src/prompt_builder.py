def montar_prompt(instrucao, contexto, input_dados, formato_output):

    if not instrucao or not input_dados:
        raise ValueError("Prompt inválido")

    prompt = f"""
INSTRUÇÃO:
{instrucao}

CONTEXTO:
{contexto}

ENTRADA:
{input_dados}

FORMATO DA RESPOSTA:
{formato_output}
"""
    return prompt



def adicionar_exemplos(prompt, exemplos):

    texto_exemplos = "\n\nEXEMPLOS:\n"

    for ex in exemplos:
        texto_exemplos += (
            f'Input: {ex["input"]}\n'
            f'Output: {ex["output"]}\n\n'
        )

    return texto_exemplos + prompt


def adicionar_cot(prompt, passos):

    texto = "\nPENSE PASSO A PASSO:\n"

    for i, passo in enumerate(passos, start=1):
        texto += f"{i}. {passo}\n"

    return texto + prompt

