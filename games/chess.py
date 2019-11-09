from game import Game
import chess
import chess.svg
import chess.pgn
from chess import Board



class Chess(Game):
    LABELS = ['W', 'B']

    def __init__(self, state=None, is_first_agent_turn=True, moves_limit=None):
        super().__init__(state, is_first_agent_turn, moves_limit)
        if state is None:
            self.state = chess.Board()
        else:
            self.state = chess.Board(state)

    def move2state(self, step):
        self.state.push(step)
        return self.state

    def get_possible_next_steps(self, limit=None):
        return list(self.state.legal_moves)

    def is_final_state(self):
        return self.state.is_game_over()

    def picture(self):
        print(self.state)

    def state_hash(self):
        return self.state.fen()

    def evaluate(self):
        if self.state.is_checkmate():
            if self.state.turn:
                return 'B'
            else:
                return 'W'
        if self.state.is_stalemate():
            return 'draw'
        if self.state.is_insufficient_material():
            return 'draw'

        return None
