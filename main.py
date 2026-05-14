from dotenv import load_dotenv
from src.tasks import tarefas
from src.techniques import (
    zero_shot,
    few_shot,
    chain_of_thought,
    role_prompting
)
from src.llm_client import LLMClient
from src.evaluator import medir_acuracia
from src.report import gerar_tabela, gerar_graficos

import json

load_dotenv()

client = LLMClient()

with open("data/inputs.json", "r", encoding="utf-8") as f:
    inputs = json.load(f)

resultados = []

for tarefa in tarefas:
    nome = tarefa["nome"]

    for item in inputs[nome]:
        texto = item['input']
        esperado = item['esperado']


        tecnicas = {
            "ZeroShot": zero_shot(tarefa, texto),
            "FewShot": few_shot(tarefa, texto),
            "CoT": chain_of_thought(tarefa, texto),
            "Role": role_prompting(tarefa, texto)
        }

        for tecnica, prompt_data in tecnicas.items():

            if tecnica == "Role":
                system_prompt, user_prompt = prompt_data
            else:
                system_prompt = ""
                user_prompt = prompt_data
            
            resposta = client.chat(
                prompt=user_prompt,
                system=system_prompt,
                temp=0.5,
                max_tokens=300
            )

            acuracia = medir_acuracia(
                resposta["resposta"],
                esperado
            )
            resultados.append({
                "tarefa": nome,
                "tecnica": tecnica,
                "input": texto,
                "esperado": esperado,
                "resposta": resposta["resposta"],
                "acuracia": acuracia,
                "tokens_prompt": resposta["tokens_prompt"],
                "tokens_resposta": resposta["tokens_resposta"],
                "tempo_ms": resposta["tempo_ms"]
            })


gerar_tabela(resultados)
gerar_graficos(resultados)

print("Execução finalizada.")
                
