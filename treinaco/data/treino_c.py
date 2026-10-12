"""Treino C. Edite a lista abaixo para alterar exercícios, séries e dicas."""

TREINO_C = {
    "id": "c",
    "titulo": "Posterior, Peito & Bíceps",
    "apelido": "Full Finish",
    "subtitulo": "Um treino completo para fechar o ciclo.",
    "foco": "Posterior + Peito + Bíceps",
    "estimulo": "Ombros",
    "duracao": "~50 min",
    "imagem": "treino-c.png",
    "numero": "03",
    "exercicios": [
        {
            "id": "stiff", "nome": "Terra Romeno com Halteres", "musculo": "Posterior e glúteos", "equipamento": "Halteres",
            "series": 3, "repeticoes": "8–10", "descanso": 90, "cadencia": "3s descida · 1s subida",
            "gif": "stiff.gif", "estimulo": False,
            "dicas": ["Mantenha leve flexão dos joelhos e halteres próximos às pernas.", "Leve o quadril para trás preservando a coluna neutra.", "Suba estendendo o quadril sem projetar a lombar para trás."],
            "evitar": "Não arredonde as costas para alcançar o chão.",
        },
        {
            "id": "flexora", "nome": "Cadeira ou Mesa Flexora", "musculo": "Posterior de coxa", "equipamento": "Cadeira/mesa flexora",
            "series": 3, "repeticoes": "10–12", "descanso": 75, "cadencia": "1s flexão · 1s pausa · 2s volta",
            "gif": "flexora.gif", "estimulo": False,
            "dicas": ["Ajuste a máquina para que o joelho se alinhe ao eixo do movimento.", "Flexione os joelhos mantendo o tronco apoiado.", "Retorne de maneira controlada."],
            "evitar": "Evite tirar o quadril do assento ou do banco.",
        },
        {
            "id": "supino", "nome": "Supino Reto com Halteres", "musculo": "Peito", "equipamento": "Banco + halteres",
            "series": 3, "repeticoes": "8–12", "descanso": 90, "cadencia": "3s descida · 1s subida",
            "gif": "supino.gif", "estimulo": False,
            "dicas": ["Deite-se com os pés firmes e escápulas estáveis no banco.", "Desça os halteres com cotovelos em trajetória confortável.", "Empurre para cima sem bater os halteres."],
            "evitar": "Não deixe o ombro rodar para uma posição dolorosa.",
        },
        {
            "id": "crucifixo", "nome": "Crucifixo no Crossover", "musculo": "Peito", "equipamento": "Cross-over",
            "series": 2, "repeticoes": "12–15", "descanso": 60, "cadencia": "1s fecha · 1s pausa · 2s abre",
            "gif": "crucifixo.gif", "estimulo": False,
            "dicas": ["Coloque as polias em altura adequada ao seu conforto.", "Mantenha uma leve flexão dos cotovelos.", "Aproxime as mãos à frente do corpo, controlando a volta."],
            "evitar": "Não estique os braços rígidos nem leve os ombros além da amplitude confortável.",
        },
        {
            "id": "rosca", "nome": "Rosca Direta com Barra", "musculo": "Bíceps", "equipamento": "Barra",
            "series": 3, "repeticoes": "10–12", "descanso": 60, "cadencia": "1s subida · 2s descida",
            "gif": "rosca.gif", "estimulo": False,
            "dicas": ["Mantenha os cotovelos próximos ao corpo.", "Flexione os braços sem inclinar o tronco para trás.", "Desça devagar até quase estender os cotovelos."],
            "evitar": "Não balance o tronco para ganhar impulso.",
        },
        {
            "id": "lateral", "nome": "Elevação Lateral com Halteres", "musculo": "Ombros", "equipamento": "Halteres",
            "series": 2, "repeticoes": "12–15", "descanso": 45, "cadencia": "1s subida · 1s pausa · 2s descida",
            "gif": "lateral.gif", "estimulo": True,
            "dicas": ["Eleve os braços pelos lados com uma leve flexão dos cotovelos.", "Suba até uma altura confortável, sem compensar com o pescoço.", "Desça os halteres lentamente."],
            "evitar": "Não eleve os ombros em direção às orelhas.",
        },
    ],
}
