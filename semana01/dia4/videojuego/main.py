import pygame
import sys

ANCHO = 640
ALTO = 480
FONDO = (0,0,64)

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
        #establecer velocidad
        self.speed = [3,3]

    def update(self):
        #Evitar que la bolita sala de la pantalla
        if self.rect.bottom >= ALTO or self.rect.top <= 0:
            self.speed[1] = -self.speed[1]
        elif self.rect.right >= ANCHO or self.rect.left <= 0:
            self.speed[0] = -self.speed[0]
        self.rect.move_ip(self.speed)

pantalla = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption('mi primer videojuego en python')

reloj = pygame.time.Clock()

bolita = Bolita()

while True:
    #establecer el reloj
    reloj.tick(60)
    #revisar todos los eventos dentro de pygame
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
    #mover  la bolita
    bolita.update()
    #pintar la pantalla
    pantalla.fill(FONDO)
    #dibujar la bolita en la pantalla
    pantalla.blit(bolita.image,bolita.rect)
    pygame.display.flip()
