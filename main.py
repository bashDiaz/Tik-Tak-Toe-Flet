import flet as ft
from game import Game
from board import Slot


def main(page: ft.Page):
    page.title = 'Tic Tac Toe'
    page.bgcolor = ft.colors.DEEP_PURPLE_200

    cards = [Slot(page) for _ in range(9)]
    card_elements = [element.generate_card() for element in cards]

    card_rows = ft.Column(
        controls=[ft.ResponsiveRow(card_elements)])

    page.add(card_rows) 
    game = Game(page)
    game.input_cards(cards)
    game.main_loop()

ft.app(target=main)