# BLUE REP — Treino ABC em Python

Um site de treino responsivo, com visual pixel art azul. Construído com **Flask + Jinja + CSS + JavaScript puro** e preparado para publicar na **Vercel**. Sem banco de dados, contas ou Node.js.

## O que já funciona

- Página inicial com os treinos A, B e C.
- Página de cada treino com os exercícios, séries, repetições, cadência, descanso, dicas e erros comuns.
- **17 GIFs autorais de estilo pixel art**, esquemáticos e ilustrativos. **Não representam demonstrações biomecânicas precisas**; para uso instrucional, substitua por vídeos reais revisados por profissional.
- Marcações de séries, registro de carga (kg) e barra de progresso; dados salvos no **localStorage do navegador**.
- Cronômetro de descanso com pausa, retomada e encerramento.
- Layout adaptado para celular.

## Estrutura

```text
blue-rep/
├── app.py                          # Main: inicializa o site Flask
├── website/
│   └── __init__.py                 # Rotas da home e dos treinos
├── data/
│   ├── __init__.py                 # Lista que cadastra os treinos
│   ├── treino_a.py                 # Exercícios do treino A
│   ├── treino_b.py                 # Exercícios do treino B
│   └── treino_c.py                 # Exercícios do treino C
├── templates/
│   ├── base.html                   # Cabeçalho, navegação, rodapé
│   ├── index.html                  # Página inicial
│   ├── workout.html                # Página interna do treino
│   ├── 404.html
│   └── components/
│       ├── workout_card.html       # Card de treino reutilizável
│       └── exercise_card.html      # Card de exercício reutilizável
├── public/
│   └── assets/
│       ├── styles/main.css         # Tema e responsividade
│       ├── scripts/app.js          # Checklists, carga e cronômetro
│       ├── images/                 # Imagens dos treinos + mascote
│       └── gifs/                   # Arquivos GIF de cada exercício
├── tools/generate_art.py           # Script OPCIONAL que gera as artes
├── tests/test_routes.py            # Testes básicos
├── requirements.txt
├── .python-version
└── .gitignore
```

## Como rodar no Windows (PowerShell)

Requer Python 3.12+ instalado.

```powershell
cd blue-rep
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Abra **http://127.0.0.1:5000**. Se o PowerShell não deixar ativar o ambiente virtual, é possível usar diretamente `\.venv\Scripts\python.exe -m pip install -r requirements.txt` e `\.venv\Scripts\python.exe app.py`.

No macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Para encerrar o servidor: `Ctrl + C`.

## Alterar um treino

Abra `data/treino_a.py`, `data/treino_b.py` ou `data/treino_c.py`. Cada arquivo contém um dicionário Python com os dados do treino, e uma lista `exercicios`. Por exemplo:

```python
{
    "id": "goblet",
    "nome": "Agachamento Goblet",
    "musculo": "Quadríceps e glúteos",
    "equipamento": "Halter",
    "series": 4,
    "repeticoes": "8–10",
    "descanso": 90,                    # Segundos
    "cadencia": "3s descida · 1s subida",
    "gif": "goblet.gif",
    "estimulo": False,
    "dicas": ["Segure o halter junto ao peito."],
    "evitar": "Não deixe os joelhos colapsarem para dentro.",
}
```

Para mudar séries e repetições, altere somente os campos; os componentes atualizam automaticamente. Para incluir um exercício, copie um dos dicionários dentro de `exercicios`, personalize as informações e inclua o arquivo GIF com o nome correspondente em `public/assets/gifs/`.

Para cadastrar **Treino D**, crie `data/treino_d.py` definindo `TREINO_D` com o mesmo formato de A, B e C. Depois, em `data/__init__.py`, importe `TREINO_D` e acrescente-o à lista `TREINOS`. Adicione uma imagem de capa em `public/assets/images/` e aponte no campo `imagem`. A navegação e os cards são gerados automaticamente.

**Aviso:** ao alterar IDs de exercícios ou de treinos, os registros anteriores do navegador podem não corresponder mais aos novos exercícios. Prefira manter IDs estáveis.

## Como colocar GIFs de execução reais

As animações incluídas são artes demonstrativas, não vídeos reais. Para substituí-las:

1. Grave ou obtenha uma animação ou vídeo com autorização de uso, idealmente validado por profissional.
2. Copie o GIF para `public/assets/gifs/` com o nome usado no exercício.
3. Se necessário, troque o campo `"gif": "arquivo.gif"` no Python.

Para arquivos `.mp4` ou `.webm` em loop, adapte a tag `<img>` em `templates/components/exercise_card.html` para `<video autoplay muted loop playsinline>` e ajuste o caminho do arquivo. Vídeos curtos costumam ser mais leves do que GIFs equivalentes.

Os GIFs pixelados incluídos podem ser **recriados** com `pip install Pillow` e `python tools/generate_art.py` (Pillow só é necessário para recriar as imagens, não para rodar o site).

## Publicar na Vercel

A Vercel reconhece automaticamente projetos Flask quando existe `app.py` exportando a variável `app`.

1. Crie um repositório vazio no GitHub e envie os arquivos deste projeto (não envie a `.venv`).
2. Abra [vercel.com/new](https://vercel.com/new), selecione **Import Git Repository** e escolha esse repositório.
3. Confirme a **Root Directory** como a pasta que contém `app.py`. Se o repositório contiver somente os arquivos deste projeto, use `./`.
4. Não é necessário escolher Next.js, adicionar um `build command` nem criar `vercel.json`. Se detectado, utilize o preset **Flask**.
5. Clique em **Deploy**. Os arquivos em `public/assets` serão disponibilizados na CDN da Vercel.

A Vercel tem documentação oficial para Flask: https://vercel.com/docs/frameworks/backend/flask

> Na Vercel, `public/` é distribuído como conteúdo estático. A rota `/assets/<path:filename>` do Flask existe para você usar as mesmas URLs em desenvolvimento local.

## Limitações conscientes desta versão

- Os dados de séries e pesos **ficam no próprio navegador**; apagar os dados do site, usar outro celular ou navegar no modo privado pode eliminá-los.
- Não existe login, sincronização em nuvem, banco ou persistência no servidor.
- O tempo aproximado de 50 min depende dos descansos, preparação, aquecimento e da velocidade de execução.
- As animações são **ilustrativas**. Confie na orientação de um profissional e respeite limitações individuais.

## Testar as rotas

```bash
python -m unittest discover -s tests -v
```

## Autorias e dependências

Arquivos, layout e ilustrações desta versão são originais. O CSS importa as fontes públicas Google Fonts (`Press Start 2P` e `Space Grotesk`) pela internet; se elas estiverem indisponíveis, entram fontes alternativas.
