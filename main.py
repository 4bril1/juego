import pygame
from personaje import personaje
import constantes
player = personaje(50, 50)
pygame.init()
ancho=constantes.ANCHO_VENTANA
alto=constantes.ALTO_VENTANA
ventana = pygame.display.set_mode((ancho, alto))
run = True
while run:
    player.dibujar(ventana)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("Izquierda")
            if event.key == pygame.K_d:
                print("Derecha")
            if event.key == pygame.K_w:
                print("Arriba")
            if event.key == pygame.K_s:
                print("Abajo")

    pygame.display.update()
pygame.quit()
