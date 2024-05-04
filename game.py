import random
import flet as ft
import os


class Game:

    _turn = 1
    _cards = None
    _cnt = True

    def __init__(self, page):
        self.page = page

    @staticmethod
    def input_cards(cards):
        Game._cards = cards

    @staticmethod
    def get_current_player():
        return 'X' if Game._turn % 2 != 0 else 'O'

    def computer_move(self):
        empty_cards = [card for card in self._cards if card.img.src == os.path.join(os.getcwd(), 'Tic_Tac_Toe\\img\\empty.png')]
        if empty_cards:
            selected_card = random.choice(empty_cards)
            selected_card.img.src = os.path.join(os.getcwd(), 'Tic_Tac_Toe\\img\\o.png')  # Change the state directly without invoking the click event
            Game._turn += 1

    def check_winner(self):
        player_value = self.get_current_player() 
        values = [card.img.src for card in self._cards]
        values = ['O' if value == os.path.join(os.getcwd(), 'Tic_Tac_Toe\\img\\o.png') else value for value in values]
        values = ['X' if value == os.path.join(os.getcwd(), 'Tic_Tac_Toe\\img\\ex.png') else value for value in values]
        values = ['' if value == os.path.join(os.getcwd(), 'Tic_Tac_Toe\\img\\empty.png') else value for value in values]

        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
            [0, 4, 8], [2, 4, 6]              # Diagonal
        ]
        
        for combination in winning_combinations:
            if all(values[idx] == player_value for idx in combination):
                print(f'Player {player_value} wins!')
                self.game_over()
                return True  # Indicar que hay un ganador
        
        return False  # Indicar que no hay ganador aún

    
    def game_over(self):
        Game._cnt = False
        dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Game over!"),
        content=ft.Text("Game Over! Do you want to play again?"),
        actions_alignment=ft.MainAxisAlignment.END,
        )
        self.page.dialog = dlg_modal
        dlg_modal.open = True

    def main_loop(self):
        while True:  # Continuar hasta que haya un ganador o un empate
            if self.check_winner():
                break

            current_player = self.get_current_player()

            if current_player == 'O':
                self.computer_move()  # Dejar que la computadora realice su movimiento
                if self.check_winner():  # Verificar si la computadora ha ganado después de su movimiento
                    break

            self.page.update()

            if not Game._cnt:  # Detener el bucle si el juego ha terminado
                break