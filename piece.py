class Piece:

    RED_MOVES = [(-1, 1), (-1, -1)]
    WHITE_MOVES = [(1, 1), (1, -1)]

    def __init__(self, color, pos, board):
        self.color = color
        self.board = board
        self.row, self.col = pos

    def get_valid_moves(self, jump_only=False):
        jump_moves = self.get_valid_jump_moves()
        if jump_moves:
            return True, jump_moves
        elif jump_only:
            return False, []
        slide_moves = self.get_valid_slide_moves()
        return False, slide_moves
        
    def get_valid_slide_moves(self):
        valid_moves = []
        for delta in self.deltas:
            delta_pos = self.get_delta_pos(delta)
            if not delta_pos:
                continue
            
            new_piece = self.board.get_pos(delta_pos)
            if new_piece is None:
                valid_moves.append(delta_pos)

        return valid_moves

    def get_valid_jump_moves(self):
        valid_moves = []
        for delta in self.deltas:
            delta_pos = self.get_delta_pos(delta)
            if delta_pos is False:
                continue
            
            next_piece = self.board.get_pos(delta_pos)

            if next_piece and next_piece.color != self.color:
                jump_pos = next_piece.get_delta_pos(delta)
                if jump_pos is not False and self.board.get_pos(jump_pos) is None:
                    valid_moves.append(jump_pos)

        return valid_moves
    
    def get_delta_pos(self, delta):
        new_row = self.row + delta[0]
        new_col = self.col + delta[1]

        if max(new_row, new_col) >= 8 or min(new_row, new_col) < 0:
            return False
        else:
            return (new_row, new_col)

    @property
    def pos(self):
        return (self.row, self.col)
        
    @property
    def display(self):
        return 'r' if self.color == 'red' else 'w' 

    @property
    def deltas(self):
        if self.color == 'red':
            return self.RED_MOVES
        elif self.color == 'white':
            return self.WHITE_MOVES