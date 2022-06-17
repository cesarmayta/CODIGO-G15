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

class Paleta(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('paleta.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = (ANCHO / 2, ALTO - 20)
        self.speed = [0,0]

    def update(self,evento):
        #Buscar si se presiono la fecha de izquierda
        if evento.key == pygame.K_LEFT and self.rect.left > 0:
            self.speed = [-5,0]
        elif evento.key == pygame.K_RIGHT and self.rect.right < ANCHO:
            self.speed = [5,0]
        else:
            self.speed = [0,0]

        self.rect.move_ip(self.speed)
    
class Ladrillo(pygame.sprite.Sprite):
    def __init__(self,posicion):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('ladrillo.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = posicion

class Muro(pygame.sprite.Group):
    def __init__(self,cantidad):
        pygame.sprite.Group.__init__(self)

        pos_x = 0
        pos_y = 20
        for i in range(cantidad):
            ladrillo = Ladrillo((pos_x,pos_y))
            self.add(ladrillo)

            pos_x += ladrillo.rect.width
            if pos_x >= ANCHO:
                pos_x = 0
                pos_y += ladrillo.rect.height

pantalla = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption('mi primer videojuego en python')

reloj = pygame.time.Clock()

#ajustar repetición de evento de tecla presionada
pygame.key.set_repeat(30)

bolita = Bolita()
jugador = Paleta()
muro = Muro(50)

while True:
    #establecer el reloj
    reloj.tick(60)
    #revisar todos los eventos dentro de pygame
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            jugador.update(evento)
    #mover  la bolita
    bolita.update()
    #pintar la pantalla
    pantalla.fill(FONDO)
    #dibujar la bolita en la pantalla
    pantalla.blit(bolita.image,bolita.rect)
    pantalla.blit(jugador.image,jugador.rect)
    muro.draw(pantalla)
    pygame.display.flip()
