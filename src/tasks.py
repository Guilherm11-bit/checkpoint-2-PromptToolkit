tarefas = [
    
    {
    "nome": "classificacao_sentimento",
    "tipo": "classificacao",
    "instrucao": "Classifique o sentimento.",
    "formato_output": "Responda apenas POSITIVO ou NEGATIVO.",

    "exemplos_fewshot": [
        {
            "input": "Produto ótimo",
            "output": "POSITIVO"
        }
    ],

    "passos_cot": [
        "Analise palavras positivas",
        "Analise palavras negativas",
        "Defina o sentimento"
    ],

    "persona": "analista_cx"
},
    {
        "nome": "extracao_produto",
        "tipo": "extracao",
        "instrucao": "Extraia produto, preço e defeito.",
        "formato_output": "Responda em JSON.",
        "exemplos_fewshot": [
            {
                "input": "Notebook Dell de R$3000 com tela quebrada",
                "output": '{"produto":"Notebook Dell","preco":"R$3000","defeito":"tela quebrada"}'
            }
        ],
        "passos_cot": [
            "Identifique o produto",
            "Identifique o preço",
            "Identifique o defeito"
        ],
        "persona": "especialista_dados"
    },

 {
        "nome": "geracao_email",
        "tipo": "geracao",
        "instrucao": "Crie um email profissional.",
        "formato_output": "Texto formal.",
        "exemplos_fewshot": [
            {
                "input": "Pedido atrasado",
                "output": "Prezado cliente..."
            }
        ],
        "passos_cot": [
            "Entenda o problema",
            "Crie saudação",
            "Explique solução"
        ],
        "persona": "especialista_suporte"
    }
]

