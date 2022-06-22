import sys
import os
import pygame as pg

from . import ANCHO, ALTO, COLOR_TEXTO, COLOR_FONDO, FPS
from .entidades import Raqueta 

class Escena:
    def __init__(self, pantalla: pg.Surface):
        self.pantalla = pantalla
        self.reloj = pg.time.Clock()

    def bucle_principal(self):
        '''Este metodo debe ser implementado por cada una de las escenas
        en funcion de lo que esten esperando hasta la condición de salida.'''
        pass
        
class Portada(Escena):
    def __init__(self, pantalla: pg.Surface):
        super().__init__(pantalla)
        self.logo = pg.image.load(
            os.path.join("resources", "images", "arkanoid_name.png"))
        font_file = os.path.join("resources", "fonts", "CabinSketch-Bold.ttf")
        self.mensaje_start_font = pg.font.Font(font_file, 30)
        
    def bucle_principal(self):        
        '''Este es el bucle principal.'''
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    salir = True                   
                
                if event.type == pg.QUIT:
                    sys.exit()
                        
            self.pantalla.fill((COLOR_FONDO))
            self.pintar_logo()
            self.pintar_texto()
            pg.display.flip()
            
    def pintar_logo(self):
            ancho_logo = self.logo.get_width()
            pos_x = (ANCHO - ancho_logo)/2
            pos_y = ALTO / 3
            self.pantalla.blit(self.logo, (pos_x, pos_y))
            
    def pintar_texto(self):
        mensaje_start = "-Pulse 'Barra Espaciadora' para comenzar-"
        texto = pg.font.Font.render(self.mensaje_start_font, mensaje_start, True, COLOR_TEXTO)
        ancho_texto = texto.get_width()
        pos_x = (ANCHO - ancho_texto)/2
        pos_y = ALTO - 100
        self.pantalla.blit(texto, (pos_x, pos_y))
            
class Partida(Escena):
    def __init__(self, pantalla: pg.Surface):
        super().__init__(pantalla)
        bg_file = os.path.join("resources", "images", "background.jpg")
        self.fondo = pg.image.load(bg_file)   
        self.jugador = Raqueta(self)     

    def pintar_fondo(self):
        self.pantalla.blit(self.fondo, (0,0))

    def bucle_principal(self):
        '''Este es el bucle principal.'''
        self.salir = False
        while not self.salir:
            self.reloj.tick(FPS)            # Seteo del tempo del juego
            
            self.revisa_eventos()           # Revisa los eventos pulsaciones y demás
            self.pintar_fondo()             
            self.jugador.update()           # Refresca ubicacion y sprite del jugador
            self.jugador.blitPala()         # Pinta al jugador
            pg.display.flip()

    def revisa_eventos(self):
        ''' Esto va revisar si hay eventos en el bucle principal'''
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self.revisa_keydown(event)
            elif event.type == pg.KEYUP:
                self.revisa_upkey(event)           
            
    def revisa_keydown(self, event):
        '''Responde a las PULSACIONES de las teclas'''
        if event.key == pg.K_RIGHT:
            self.jugador.mueve_derecha = True
        elif event.key == pg.K_LEFT:
            self.jugador.mueve_izquierda = True
        elif event.key == pg.K_SPACE:
            self.salir = True
        
    def revisa_upkey(self, event):
        '''Responde a las LIBERACIONES de las teclas'''
        if event.key == pg.K_RIGHT:
            self.jugador.mueve_derecha = False
        if event.key == pg.K_LEFT:
            self.jugador.mueve_izquierda = False
        

class HallOfFame(Escena):
    def bucle_principal(self):
        '''Este es el bucle principal.'''
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    salir = True                   
                
                if event.type == pg.QUIT:
                    sys.exit()
                
            self.pantalla.fill((0, 99, 0))
            pg.display.flip()
