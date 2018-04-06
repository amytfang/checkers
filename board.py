from piece     import Piece

class Board:

    def __init__(self):
        self._generate_game_board()

    def _generate_game_board(self):
        grid = []

        for row in range(8):
            grid.append([])
            for col in range(8):
                if row <= 2 and (row + col) % 2 != 0:
                    grid[row].append(Piece('white', (row, col), self))
                elif row >= 5 and (row + col) % 2 != 0:
                    grid[row].append(Piece('red', (row, col), self))
                else: 
                    grid[row].append(None)

        self.board = grid

    def print_board(self):
        print('  0 1 2 3 4 5 6 7')
        for idx, row in enumerate(self.board):
            display_row = ' '.join([piece.display if piece else '_' for piece in row])
            print(str(idx) + " " + display_row)

    def move_piece(self, piece, to_pos):
        
        self.board[to_pos[0]][to_pos[1]] = piece
        self.board[piece.row][piece.col] = None

        if abs(to_pos[0] - piece.row) > 1:
            self.remove_jumped_piece(to_pos, piece.pos)

        piece.row, piece.col = to_pos

    def remove_jumped_piece(self, pos1, pos2):
        jumped_row = int((pos1[0] + pos2[0]) / 2)
        jumped_col = int((pos1[1] + pos2[1]) / 2)
        self.board[jumped_row][jumped_col] = None

    def get_pos(self, pos):
        return self.board[pos[0]][pos[1]]

    def get_valid_moves(self, color):
        valid_moves = {}

        jump_only = False
        for row in range(8):
            for col in range(8):
                piece = self.get_pos((row,col))
                if piece and piece.color == color:
                    jump, moves = piece.get_valid_moves(jump_only)

                    if jump and not jump_only:
                        jump_only = True
                        valid_moves = {piece.pos: moves}
                    elif moves:
                        valid_moves[piece.pos] = moves
        
        return jump_only, valid_moves

        
                