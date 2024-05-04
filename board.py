import flet as ft
from game import Game

import os


class Slot:

    _id = 1

    def __init__(self, page):
        self.page = page
        self.img = ft.Image(
            src = os.path.join(os.getcwd(), 'Tic_Tac_Toe\\img\\empty.png'),
            width = 100,
            height = 100,
            fit=ft.ImageFit.CONTAIN)
        self.id = Slot._id
        Slot._id += 1

    def on_click(self, e):
        if Game._cnt:  # Solo permitir movimientos si el juego no ha terminado
            if self.img.src == os.path.join(os.getcwd(), 'Tic_Tac_Toe\\img\\empty.png'):
                if Game.get_current_player() == 'X':
                    self.img.src = os.path.join(os.getcwd(), 'Tic_Tac_Toe\\img\\ex.png')
                    Game._turn += 1
                    self.page.update()  # Asegurarse de que la actualización de la página ocurra después de cada movimiento válido
            else:
                print('Card already taken')



    def hover(self, e):
        self.card.bgcolor = ft.colors.DEEP_PURPLE_400 if e.data == 'true' else ft.colors.DEEP_PURPLE_300
        self.page.update()

    def generate_card(self):
        self.img.src = os.path.join(os.getcwd(), 'Tic_Tac_Toe\\img\\empty.png')
        self.card =  ft.Container(
                width=100,
                height=self.page.height/3.2,
                bgcolor=ft.colors.DEEP_PURPLE_300,
                content=self.img,
                col={'sm':4},
                on_click=self.on_click,
                on_hover=self.hover,
            )
        return self.card