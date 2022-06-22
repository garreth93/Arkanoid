import os

import pygame as pg
from pygame.sprite import Sprite

from . import ALTO, ANCHO, SPEED_PALA


class Raqueta(Sprite):
    margen_inferior = 20

    def __init__(self, ai_game):
        super().__init__()
        self.pantalla = ai_game.pantalla
        self.pantalla_rect = ai_game.pantalla.get_rect()

        self.sprites = [
            pg.image.load(os.path.join("resources", "images", "electric00.png")),
            pg.image.load(os.path.join("resources", "images", "electric01.png")),
            pg.image.load(os.path.join("resources", "images", "electric02.png"))
        ]

        self.contador = 0

        image_path = os.path.join("resources", "images", "electric00.png")
        self.image = pg.image.load(image_path)
        self.rect = self.image.get_rect(midbottom=(ANCHO/2, ALTO - self.margen_inferior))

        # Guardado valor decimal para la posición horizontal de la pala
        self.x = float(self.rect.x)

        # Chivatos de movimiento
        self.mueve_derecha = False
        self.mueve_izquierda = False


    def update(self):
        self.image = self.sprites[self.contador]
        self.contador += 1
        if self.contador > 2:
            self.contador = 0
        
        if self.mueve_derecha and self.rect.right < self.pantalla_rect.right:
            self.x += SPEED_PALA
        if self.mueve_izquierda and self.rect.left > 0:
            self.x -= SPEED_PALA

        self.rect.x = self.x

    def blitPala(self):
        self.pantalla.blit(self.image, self.rect)