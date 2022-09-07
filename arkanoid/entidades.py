import os

import pygame as pg
from pygame.sprite import Sprite

from . import ALTO, ANCHO, SPEED_PALA, FPS


class Raqueta(Sprite):
    margen_inferior = 20
    velocidad = 5
    fps_animacion = 12
    limite_iteracion = FPS // fps_animacion
    iteracion = 0

    def __init__(self, ai_game):
        super().__init__()
        self.pantalla = ai_game.pantalla
        self.pantalla_rect = ai_game.pantalla.get_rect()

        self.sprites = []
        for i in range(3):
            self.sprites.append(
                pg.image.load(
                    os.path.join("resources", "images", f"electric0{i}.png")
                )
            )

        self.siguiente_imagen = 0
        self.image = self.sprites[self.siguiente_imagen]
        self.rect = self.image.get_rect(midbottom=(ANCHO/2, ALTO - self.margen_inferior))

        # Guardado valor decimal para la posición horizontal de la pala
        self.x = float(self.rect.x)

        # Chivatos de movimiento
        self.mueve_derecha = False
        self.mueve_izquierda = False


    def update(self):    
        self.iteracion += 1
        if self.iteracion == self.limite_iteracion:
            self.siguiente_imagen += 1
            if self.siguiente_imagen >= len(self.sprites):
                self.siguiente_imagen = 0
            self.image = self.sprites[self.siguiente_imagen]
            self.iteracion = 0
        
        if self.mueve_derecha and self.rect.right < self.pantalla_rect.right:
            self.x += SPEED_PALA
        if self.mueve_izquierda and self.rect.left > 0:
            self.x -= SPEED_PALA

        self.rect.x = self.x

    def blitPala(self):
        self.pantalla.blit(self.image, self.rect)

class Ladrillo(Sprite):
    def __init__(self, fila, columna):
        super().__init__()

        ladrillo_verde = os.path.join("resources", "images", "greenTile.png")
        self.image = pg.image.load(ladrillo_verde)
        ancho = self.image.get_width()
        alto = self.image.get_height()

        self.rect = self.image.get_rect(x=columna * ancho, y=fila* alto)


class Pelota(Sprite):

    velocidad_x = -5
    velocidad_y = -5

    def __init__(self, **kwargs):
        super().__init__()
        self.image = pg.image.load(
            os.path.join("resources", "images", "ball1.png")
        )
        self.rect = self.image.get_rect(**kwargs)

    def update(self, raqueta, juego_iniciado):
        if not juego_iniciado:
            self.rect = self.image.get_rect(midbottom=raqueta.rect.midtop)
        else:
            self.rect.x += self.velocidad_x
            if self.rect.right > ANCHO or self.rect.left < 0:
                self.velocidad_x = -self.velocidad_x

            self.rect.y += self.velocidad_y
            if self.rect.top <= 0:
                self.velocidad_y = -self.velocidad_y

            if self.rect.top > ALTO:
                self.pierdes()
                self.reset()

    def pierdes(self):
        print("Pierdes una vida")

    def reset(self):
        print("Recolocamos la pelota en su posición inicial")

    def hay_colision(self, otro):
        if self.rect.colliderect(otro):
            # hay colisión
            self.velocidad_y = -self.velocidad_y