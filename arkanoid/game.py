import os
import pygame as pg

from arkanoid.escenas import Portada, Partida, HallOfFame
from arkanoid import ALTO, ANCHO

class Arkanoid:
    def __init__(self):
        print('Arranca el juego')
        pg.init()
        self.display = pg.display.set_mode((ANCHO, ALTO))
        pg.display.set_caption('Arkanoid')
        
        icon = pg.image.load(os.path.join("resources", "images", "iconArk.png"))
        pg.display.set_icon(icon)
        
        self.escenas = [
            Portada(self.display),
            Partida(self.display),
            HallOfFame(self.display),
        ]
        
    def jugar(self):
        for escena in self.escenas:
            escena.bucle_principal()
                        
            

