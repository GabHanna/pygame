import pygame
import time

# Definindo as constantes de cores com o sistema RGB
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# Definindo constante da dimensão da tela
LARGURAJANELA = 800
ALTURAJANELA = 700

# Definindo a funcao mover
def mover (figura, dimensaoJanela):
    borda_esquerda = 0
    borda_superior = 0
    borda_direita = dim_janela[0]
    borda_inferior = dim_janela[1]

# Checa se figura ultrapassa o topo ou base da janela
if figura["objRect"].top < borda_superior or figura ["objRect"].bottom > borda_inferior:
    # Figura atingiu o topo ou a base da janela
    # Se sim, então inverte o valor de velocidade. Efeito visual de quicar.
    figura['vel'[1] =-figura"vel"1
