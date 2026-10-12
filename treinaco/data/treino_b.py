"""Treino B. Edite a lista abaixo para alterar exercícios, séries e dicas."""

TREINO_B = {
    "id": "b",
    "titulo": "Costas & Tríceps",
    "apelido": "Upper Focus",
    "subtitulo": "Postura, estabilidade e força para o dia a dia.",
    "foco": "Costas + Tríceps",
    "estimulo": "Glúteos",
    "duracao": "~50 min",
    "imagem": "treino-b.png",
    "numero": "02",
    "exercicios": [
        {
            "id": "puxada", "nome": "Puxada Frontal", "musculo": "Costas", "equipamento": "Polia alta",
            "series": 4, "repeticoes": "8–12", "descanso": 75, "cadencia": "1s puxada · 1s pausa · 2s volta",
            "gif": "puxada.gif", "estimulo": False,
            "dicas": ["Sente-se com o tronco estável e peito levemente elevado.", "Puxe a barra na direção da parte alta do peito.", "Permita que os braços retornem com controle."],
            "evitar": "Evite puxar a barra atrás da nuca ou usar balanço excessivo.",
        },
        {
            "id": "remada", "nome": "Remada Baixa", "musculo": "Costas", "equipamento": "Polia baixa",
            "series": 3, "repeticoes": "8–12", "descanso": 75, "cadencia": "1s puxada · 1s pausa · 2s volta",
            "gif": "remada.gif", "estimulo": False,
            "dicas": ["Mantenha a coluna neutra e o abdômen firme.", "Traga os cotovelos para trás sem elevar os ombros.", "Estenda os braços com controle para repetir."],
            "evitar": "Não transforme o movimento em um balanço exagerado do tronco.",
        },
        {
            "id": "pulldown", "nome": "Pulldown com Braços Estendidos", "musculo": "Costas", "equipamento": "Polia alta",
            "series": 2, "repeticoes": "12–15", "descanso": 60, "cadencia": "1s puxada · 1s pausa · 2s volta",
            "gif": "pulldown.gif", "estimulo": False,
            "dicas": ["Fique em pé e dê um pequeno passo para trás da polia.", "Mantenha uma leve flexão nos cotovelos.", "Traga o acessório em direção às coxas sem curvar as costas."],
            "evitar": "Evite dobrar e estender excessivamente os cotovelos para mover a carga.",
        },
        {
            "id": "triceps-corda", "nome": "Tríceps na Polia com Corda", "musculo": "Tríceps", "equipamento": "Polia + corda",
            "series": 3, "repeticoes": "10–15", "descanso": 60, "cadencia": "1s extensão · 1s pausa · 2s volta",
            "gif": "triceps-corda.gif", "estimulo": False,
            "dicas": ["Mantenha os cotovelos próximos ao tronco.", "Estenda os braços mantendo ombros estáveis.", "Deixe a corda subir devagar antes de repetir."],
            "evitar": "Não use o peso do corpo para empurrar a corda.",
        },
        {
            "id": "triceps-frances", "nome": "Tríceps Francês com Halter", "musculo": "Tríceps", "equipamento": "Halter",
            "series": 3, "repeticoes": "10–12", "descanso": 60, "cadencia": "3s flexão · 1s extensão",
            "gif": "triceps-frances.gif", "estimulo": False,
            "dicas": ["Segure o halter acima da cabeça com os cotovelos apontando para cima.", "Flexione os cotovelos dentro de uma amplitude confortável.", "Estenda os braços mantendo o tronco firme."],
            "evitar": "Evite abrir os cotovelos excessivamente ou forçar o ombro.",
        },
        {
            "id": "sumo", "nome": "Agachamento Sumô com Halter", "musculo": "Glúteos e adutores", "equipamento": "Halter",
            "series": 2, "repeticoes": "12–15", "descanso": 75, "cadencia": "3s descida · 1s subida",
            "gif": "sumo.gif", "estimulo": True,
            "dicas": ["Afaste os pés um pouco mais que a largura dos ombros.", "Aponte as pontas dos pés levemente para fora, conforme seu conforto.", "Desça com controle e suba mantendo os joelhos alinhados aos pés."],
            "evitar": "Não force uma abertura de quadril desconfortável.",
        },
    ],
}
