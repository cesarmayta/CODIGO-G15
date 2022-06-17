import pygame
import sys

ANCHO = 640
ALTO = 480

class Bolita(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #imagen del sprite
        self.image = pygame.image.load('bolita.png')
        #obtener el rectangulo de la imagen
        self.rect = self.image.get_rect()
        #posición inicial de la bolita
        self.rect.centerx = ANCHO / 2
        self.rect.centery = ALTO / 2

pantalla = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption('mi primer videojuego en python')

bolita = Bolita()

while True:
    #revisar todos los eventos dentro de pygame
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
    #dibujar la bolita en la pantalla
    pantalla.blit(bolita.image,bolita.rect)
    pygame.display.flip()
