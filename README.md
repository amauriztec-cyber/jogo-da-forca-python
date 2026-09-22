# Jogo da Forca em Python

Jogo da forca com interface gráfica, desenvolvido em Python puro utilizando a biblioteca `tkinter`. O jogador escolhe uma categoria, tenta adivinhar a palavra secreta letra por letra e acompanha visualmente o desenho da forca conforme os erros aumentam.

## Jogue online

🎮 [Jogar agora](https://amauriztec-cyber.github.io/jogo-da-forca-python/)

## Funcionalidades

- Seleção de categoria (tecnologia, natureza, comida) antes de cada partida
- Palavra sorteada aleatoriamente dentro da categoria escolhida, com dica exibida na tela
- Teclado virtual em grade, com feedback visual (verde para acerto, vermelho para erro)
- Desenho da forca em ASCII, atualizado a cada erro
- Detecção automática de vitória e derrota, com opção de jogar novamente
- Palavras e dicas carregadas de um arquivo `palavras.json` externo

## Conceitos praticados

- Programação orientada a eventos (`command=`, callbacks disparados por clique)
- Manipulação de variáveis dentro de closures (`lambda` e o problema clássico de variáveis capturadas em loops)
- Estruturas de dados: dicionários aninhados, `set()` para letras tentadas
- Leitura e escrita de arquivos JSON
- Organização de interface com `Frame`, `.pack()` e `.grid()`
- Tratamento de erros (`try/except` na leitura de arquivos)
- Empacotamento do script em executável standalone (`.exe`) com PyInstaller

## Como rodar

**Opção 1 — executando o código-fonte:**

```bash
python Forca2.py
```

Requer apenas Python 3 instalado (o `tkinter` já vem incluso na instalação padrão).

**Opção 2 — executável (.exe)**

Baixe o executável pronto na aba [Releases](../../releases) deste repositório e execute diretamente, sem necessidade de instalar Python.

## Tecnologias

- Python 3
- tkinter (interface gráfica)
- json (persistência de dados e histórico)
- PyInstaller (empacotamento)

## Próximos passos

- Migrar a estrutura de funções para uma classe `JogoDaForcaGUI`
- Exibir histórico e estatísticas de partidas na própria interface
- Adicionar novas categorias e palavras