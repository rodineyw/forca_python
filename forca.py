import random
from tkinter import *
from tkinter import messagebox
import tkinter

# Lista de palavras para o jogo
palavras = ["python", "programacao", "programador", "jogo", "divertido", "desafio"]


# Função para escolher palavra aleatória da lista
def escolher_palavra():
    return random.choice(palavras)


# Função para atualizar a palavra oculta na interface gráfica
def atualizar_palavra_oculta():
    global palavra_oculta
    palavra_oculta = ""
    for letra in palavra_secreta:
        if letra in letras_adivinhadas:
            palavra_oculta += letra
        else:
            palavra_oculta += "_"
    lbl_palavra.config(text=palavra_oculta)


# Função para verificar se o jogador venceu ou perdeu
def verificar_resultado():
    if palavra_oculta == palavra_secreta:
        messagebox.showinfo("Parabéns", "Você venceu!")
        janela.quit()
    elif tentativas == 0:
        messagebox.showinfo(
            "Fim de jogo", f"A palavra era '{palavra_secreta}'.Você perdeu zé ruéla!"
        )
        janela.quit()


# Função para adivinhar uma letra
def adivinhar_letra():
    global tentativas
    letra = entrada_letra.get().lower()

    if letra in letras_adivinhadas:
        messagebox.showwarning("Letra Repetida", "Você já tentou essa Letra.")
    elif letra in palavra_secreta:
        letras_adivinhadas.add(letra)
        atualizar_palavra_oculta()
        verificar_resultado()
    else:
        letras_adivinhadas.add(letra)
        tentativas -= 1
        lbl_tentativas.config(text=f"Tentativas restantes: {tentativas}")
        verificar_resultado()


# Inicialização do jogo
palavra_secreta = escolher_palavra()
letras_adivinhadas = set()
tentativas = 6

janela = tkinter.Tk()
janela.title("Jogo da Forca")

# Configurar elemeentos da interface gráfica
lbl_palavra = tkinter.Label(janela, text="", font=("Arial", 24))
lbl_palavra.pack()

entrada_letra = tkinter.Entry(janela, font=("Arial", 16))
entrada_letra.pack()

btn_adivinhar = tkinter.Button(janela, text="Adivinhar Letra", command=adivinhar_letra)
btn_adivinhar.pack()

lbl_tentativas = tkinter.Label(
    janela, text=f"Tentativas restantes: {tentativas}", font=("Arial", 16)
)
lbl_tentativas.pack()

# Começar o jogo
atualizar_palavra_oculta()
janela.mainloop()
