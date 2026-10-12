"""Treino A. Edite a lista abaixo para alterar exercícios, séries e dicas."""

TREINO_A = {
    "id": "a",
    "titulo": "Quadríceps & Glúteos",
    "apelido": "Lower Power",
    "subtitulo": "Força e controle, repetição por repetição.",
    "foco": "Quadríceps + Glúteos",
    "estimulo": "Panturrilha",
    "duracao": "~50 min",
    "imagem": "treino-a.png",
    "numero": "01",
    "exercicios": [
        {
            "id": "goblet", "nome": "Agachamento Goblet", "musculo": "Quadríceps e glúteos", "equipamento": "Halter",
            "series": 4, "repeticoes": "8–10", "descanso": 90, "cadencia": "3s descida · 1s subida",
            "gif": "goblet.gif", "estimulo": False,
            "dicas": ["Segure o halter junto ao peito e mantenha o tronco firme.", "Desça até uma amplitude confortável sem perder a posição da coluna.", "Suba pressionando o chão com todo o pé."],
            "evitar": "Evite deixar os joelhos colapsarem para dentro ou tirar os calcanhares do chão.",
        },
        {
            "id": "leg-press", "nome": "Leg Press", "musculo": "Quadríceps e glúteos", "equipamento": "Leg Press",
            "series": 3, "repeticoes": "10–12", "descanso": 90, "cadencia": "3s flexão · 1s empurrada",
            "gif": "leg-press.gif", "estimulo": False,
            "dicas": ["Mantenha lombar e quadril apoiados no encosto.", "Flexione joelhos de forma controlada, sem arredondar a lombar.", "Empurre a plataforma sem travar bruscamente os joelhos."],
            "evitar": "Não tire o quadril do banco para ganhar amplitude.",
        },
        {
            "id": "hip-thrust", "nome": "Elevação Pélvica com Halter", "musculo": "Glúteos", "equipamento": "Banco + halter",
            "series": 3, "repeticoes": "10–12", "descanso": 90, "cadencia": "2s descida · 1s subida · 2s no topo",
            "gif": "hip-thrust.gif", "estimulo": False,
            "dicas": ["Apoie a parte superior das costas em um banco estável.", "Deixe o halter confortável e seguro sobre a região do quadril.", "Eleve o quadril contraindo os glúteos sem hiperestender a lombar."],
            "evitar": "Evite jogar a cabeça para trás ou arquear demais as costas no topo.",
        },
        {
            "id": "extensora", "nome": "Cadeira Extensora", "musculo": "Quadríceps", "equipamento": "Cadeira extensora",
            "series": 3, "repeticoes": "12–15", "descanso": 60, "cadencia": "1s extensão · 1s no topo · 2s volta",
            "gif": "extensora.gif", "estimulo": False,
            "dicas": ["Ajuste banco e rolo conforme seu tamanho.", "Estenda os joelhos sem dar impulso com o tronco.", "Retorne lentamente até a posição inicial."],
            "evitar": "Não balance o corpo para levantar a carga.",
        },
        {
            "id": "panturrilha", "nome": "Panturrilha em Pé com Halteres", "musculo": "Panturrilhas", "equipamento": "Halteres",
            "series": 2, "repeticoes": "12–18", "descanso": 45, "cadencia": "1s subida · 1s no topo · 2s descida · 1s embaixo",
            "gif": "panturrilha.gif", "estimulo": True,
            "dicas": ["Mantenha um apoio próximo para o equilíbrio, se necessário.", "Suba na ponta dos pés sem flexionar demais os joelhos.", "Desça com controle e use amplitude confortável."],
            "evitar": "Não quique na parte baixa do movimento.",
        },
    ],
}
