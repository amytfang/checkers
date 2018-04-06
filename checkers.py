from board     import Board

class Checkers:

    def __init__(self):
        self.board = Board()

    @property
    def waiting_color(self):
        return 'white' if self.current_color == 'red' else 'red'

    @property
    def current_color_display(self):
        return self.current_color.capitalize()

    def swap_players(self):
        self.current_color = 'white' if self.current_color == 'red' else 'red'

    def get_player_instructions(self, purpose):
        return '{player}, enter a comma-separated row and column (e.g. "3,4" or "0,4") to {purpose}:\n'.format(
            player = self.current_color_display, purpose = purpose
        )

    def main(self):
        board = self.board
        while True:
            first_player = input('What colors plays first? Select "red" or "white"\n')
            if first_player in ['red', 'white']:
                self.current_color = first_player 
                break
            else:
                print('Invalid input.  Please try again.')

        while True:
            board.print_board()

            jumped, valid_moves = board.get_valid_moves(self.current_color)
            if not valid_moves:
                print(self.waiting_color.capitalize() + " wins!")
                break

            selected_piece = None
            while not selected_piece:
                piece_coord_str = input(self.get_player_instructions('select your piece to move'))
                piece_coord = tuple([int(i) for i in piece_coord_str.split(',')])
                if piece_coord in valid_moves:
                    selected_piece = board.get_pos(piece_coord)
                else:
                    print('Invalid selection')

            while True:
                move_coord_str = input(self.get_player_instructions('select the destination'))
                move_coord = tuple([int(i) for i in move_coord_str.split(',')])
                if move_coord in valid_moves[selected_piece.pos]:
                    board.move_piece(selected_piece, move_coord)
                    break
                else:
                    print('Invalid selection')

            if jumped:
                valid_jumps = selected_piece.get_valid_jump_moves()
                while valid_jumps:
                    board.print_board()
                    jump_coord_str = input(self.get_player_instructions('make additional jumps'))
                    jump_coord = tuple([int(i) for i in jump_coord_str.split(',')])
                    if jump_coord in valid_jumps:
                        board.move_piece(selected_piece, jump_coord)
                        valid_jumps = selected_piece.get_valid_jump_moves()
                    else:
                        print('Invalid selection')

            self.swap_players()


if __name__ == '__main__':
    game = Checkers()
    game.main()