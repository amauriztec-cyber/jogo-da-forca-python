import tkinter as tk
import string
import random

BANCO_PALAVRAS = {
    "tecnologia": {
        "python": "Linguagem de programação criada por Guido van Rossum",
        "teclado": "Periférico usado para digitar",
    },
    "natureza": {
        "montanha": "Elevação natural do terreno",
        "floresta": "Área com grande concentração de árvores",
    },
}

max_erros = 6

DESENHOS = [
    """
  ------
  |    |
  |
  |
  |
---------""",
    """
  ------
  |    |
  |    O
  |
  |
---------""",
    """
  ------
  |    |
  |    O
  |    |
  |
---------""",
    """
  ------
  |    |
  |    O
  |   /|
  |
---------""",
    """
  ------
  |    |
  |    O
  |   /|\\
  |
---------""",
    """
  ------
  |    |
  |    O
  |   /|\\
  |   /
---------""",
    """
  ------
  |    |
  |    O
  |   /|\\
  |   / \\
---------""",
]

# ---------- estado do jogo (variáveis que mudam a cada partida) ----------
palavra_secreta = ""
letras_certas = set()
letras_erradas = set()
botoes = {}


def mostrar_tela_categoria():
    frame_jogo.pack_forget()
    frame_categoria.pack()


def iniciar_jogo(categoria):
    global palavra_secreta, letras_certas, letras_erradas

    palavra, dica = random.choice(list(BANCO_PALAVRAS[categoria].items()))
    palavra_secreta = palavra
    letras_certas = set()
    letras_erradas = set()

    label_dica.config(text=f"Dica: {dica}")
    label_forca.config(text=DESENHOS[0])
    label_status.config(text="")

    montar_teclado()

    frame_categoria.pack_forget()
    frame_jogo.pack()

    atualizar_tela()


def montar_teclado():
    for widget in frame_teclado.winfo_children():
        widget.destroy()
    botoes.clear()

    for i, letra in enumerate(string.ascii_lowercase):
        btn = tk.Button(frame_teclado, text=letra, width=3)
        btn.config(command=lambda l=letra, b=btn: tentar_letra(l, b))
        btn.grid(row=i // 9, column=i % 9)
        botoes[letra] = btn


def tentar_letra(letra, botao):
    if letra in palavra_secreta:
        letras_certas.add(letra)
        botao.config(bg="lightgreen")
    else:
        letras_erradas.add(letra)
        botao.config(bg="salmon")

    botao.config(state="disabled")
    atualizar_tela()


def atualizar_tela():
    exibida = " ".join(
        letra if letra in letras_certas else "_"
        for letra in palavra_secreta
    )
    label_palavra.config(text=exibida)
    label_erros.config(text=f"Erros: {len(letras_erradas)}/{max_erros}")
    label_forca.config(text=DESENHOS[len(letras_erradas)])

    venceu = "_" not in exibida
    perdeu = len(letras_erradas) >= max_erros

    if venceu:
        label_status.config(text="Você venceu!", fg="green")
        desabilitar_teclado()
    elif perdeu:
        label_status.config(text=f"Você perdeu! Era: {palavra_secreta}", fg="red")
        desabilitar_teclado()


def desabilitar_teclado():
    for botao in botoes.values():
        botao.config(state="disabled")


# ---------- montagem da janela ----------
root = tk.Tk()
root.title("Jogo da Forca")

# --- tela 1: escolha de categoria ---
frame_categoria = tk.Frame(root)

tk.Label(frame_categoria, text="Escolha uma categoria:", font=("Courier New", 12)).pack(pady=10)

for categoria in BANCO_PALAVRAS:
    tk.Button(
        frame_categoria, text=categoria, width=16,
        command=lambda c=categoria: iniciar_jogo(c)
    ).pack(pady=3)

# --- tela 2: jogo ---
frame_jogo = tk.Frame(root)

label_forca = tk.Label(frame_jogo, font=("Courier New", 10), justify="left")
label_forca.pack(pady=8)

label_dica = tk.Label(frame_jogo, font=("Courier New", 10))
label_dica.pack()

label_palavra = tk.Label(frame_jogo, font=("Courier New", 18))
label_palavra.pack(pady=10)

label_erros = tk.Label(frame_jogo)
label_erros.pack()

label_status = tk.Label(frame_jogo, font=("Courier New", 12, "bold"))
label_status.pack(pady=8)

frame_teclado = tk.Frame(frame_jogo)
frame_teclado.pack()

tk.Button(frame_jogo, text="Jogar de novo", command=mostrar_tela_categoria).pack(pady=10)

# a tela inicial é a de categoria
frame_categoria.pack()

root.mainloop()