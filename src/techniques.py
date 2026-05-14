from src.prompt_builder import (
    montar_prompt,
    adicionar_exemplos,
    adicionar_cot
)

import json

with open("prompts/system_prompts.json", "r", encoding="utf-8") as f:
    personas = json.load(f)



def zero_shot(tarefa, texto):

    return montar_prompt(
        tarefa["instrucao"],
        "",
        texto,
        tarefa["formato_output"]
    )
def few_shot(tarefa, texto):

    prompt = montar_prompt(
        tarefa["instrucao"],
        "",
        texto,
        tarefa["formato_output"]
    )

    return adicionar_exemplos(
        prompt,
        tarefa["exemplos_fewshot"]
    )



def chain_of_thought(tarefa, texto):

    prompt = montar_prompt(
        tarefa["instrucao"],
        "",
        texto,
        tarefa["formato_output"]
    )

    return adicionar_cot(prompt, tarefa["passos_cot"])



def role_prompting(tarefa, texto):

    persona = personas[tarefa["persona"]]

    user_prompt = montar_prompt(
        tarefa["instrucao"],
        "",
        texto,
        tarefa["formato_output"]
    )

    return persona, user_prompt