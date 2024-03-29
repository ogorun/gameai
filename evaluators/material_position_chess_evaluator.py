from evaluator import Evaluator
from games.chess import Chess
import chess


class MaterialPositionChessEvaluator(Evaluator):

    def evaluate(self, game):
        """
        Taken from https://medium.com/@andreasstckl/writing-a-chess-program-in-one-day-30daff4610ec
        https://www.chessprogramming.org/Simplified_Evaluation_Function

        :param game:
        :return:
        """

        pawntable = [
            0,  0,  0,  0,  0,  0,  0,  0,
            5, 10, 10,-20,-20, 10, 10,  5,
            5, -5,-10,  0,  0,-10, -5,  5,
            0,  0,  0, 20, 20,  0,  0,  0,
            5,  5, 10, 25, 25, 10,  5,  5,
            10, 10, 20, 30, 30, 20, 10, 10,
            50, 50, 50, 50, 50, 50, 50, 50,
            0,  0,  0,  0,  0,  0,  0,  0]

        knightstable = [
            -50,-40,-30,-30,-30,-30,-40,-50,
            -40,-20,  0,  5,  5,  0,-20,-40,
            -30,  5, 10, 15, 15, 10,  5,-30,
            -30,  0, 15, 20, 20, 15,  0,-30,
            -30,  5, 15, 20, 20, 15,  5,-30,
            -30,  0, 10, 15, 15, 10,  0,-30,
            -40,-20,  0,  0,  0,  0,-20,-40,
            -50,-40,-30,-30,-30,-30,-40,-50]

        bishopstable = [
            -20,-10,-10,-10,-10,-10,-10,-20,
            -10,  5,  0,  0,  0,  0,  5,-10,
            -10, 10, 10, 10, 10, 10, 10,-10,
            -10,  0, 10, 10, 10, 10,  0,-10,
            -10,  5,  5, 10, 10,  5,  5,-10,
            -10,  0,  5, 10, 10,  5,  0,-10,
            -10,  0,  0,  0,  0,  0,  0,-10,
            -20,-10,-10,-10,-10,-10,-10,-20]

        rookstable = [
            0,  0,  0,  5,  5,  0,  0,  0,
            -5,  0,  0,  0,  0,  0,  0, -5,
            -5,  0,  0,  0,  0,  0,  0, -5,
            -5,  0,  0,  0,  0,  0,  0, -5,
            -5,  0,  0,  0,  0,  0,  0, -5,
            -5,  0,  0,  0,  0,  0,  0, -5,
            5, 10, 10, 10, 10, 10, 10,  5,
            0,  0,  0,  0,  0,  0,  0,  0]

        queenstable = [
            -20,-10,-10, -5, -5,-10,-10,-20,
            -10,  0,  0,  0,  0,  0,  0,-10,
            -10,  5,  5,  5,  5,  5,  0,-10,
            0,  0,  5,  5,  5,  5,  0, -5,
            -5,  0,  5,  5,  5,  5,  0, -5,
            -10,  0,  5,  5,  5,  5,  0,-10,
            -10,  0,  0,  0,  0,  0,  0,-10,
            -20,-10,-10, -5, -5,-10,-10,-20]

        kingstable = [
            20, 30, 10,  0,  0, 10, 30, 20,
            20, 20,  0,  0,  0,  0, 20, 20,
            -10,-20,-20,-20,-20,-20,-20,-10,
            -20,-30,-30,-40,-40,-30,-30,-20,
            -30,-40,-40,-50,-50,-40,-40,-30,
            -30,-40,-40,-50,-50,-40,-40,-30,
            -30,-40,-40,-50,-50,-40,-40,-30,
            -30,-40,-40,-50,-50,-40,-40,-30]

        wp = len(game.state.pieces(chess.PAWN, chess.WHITE))
        bp = len(game.state.pieces(chess.PAWN, chess.BLACK))
        wn = len(game.state.pieces(chess.KNIGHT, chess.WHITE))
        bn = len(game.state.pieces(chess.KNIGHT, chess.BLACK))
        wb = len(game.state.pieces(chess.BISHOP, chess.WHITE))
        bb = len(game.state.pieces(chess.BISHOP, chess.BLACK))
        wr = len(game.state.pieces(chess.ROOK, chess.WHITE))
        br = len(game.state.pieces(chess.ROOK, chess.BLACK))
        wq = len(game.state.pieces(chess.QUEEN, chess.WHITE))
        bq = len(game.state.pieces(chess.QUEEN, chess.BLACK))

        material = 100*(wp-bp)+320*(wn-bn)+330*(wb-bb)+500*(wr-br)+900*(wq-bq)

        pawnsq = sum([pawntable[i] for i in game.state.pieces(chess.PAWN, chess.WHITE)])
        pawnsq= pawnsq + sum([-pawntable[chess.square_mirror(i)]
                              for i in game.state.pieces(chess.PAWN, chess.BLACK)])
        knightsq = sum([knightstable[i] for i in game.state.pieces(chess.KNIGHT, chess.WHITE)])
        knightsq = knightsq + sum([-knightstable[chess.square_mirror(i)]
                                   for i in game.state.pieces(chess.KNIGHT, chess.BLACK)])
        bishopsq= sum([bishopstable[i] for i in game.state.pieces(chess.BISHOP, chess.WHITE)])
        bishopsq= bishopsq + sum([-bishopstable[chess.square_mirror(i)]
                                  for i in game.state.pieces(chess.BISHOP, chess.BLACK)])
        rooksq = sum([rookstable[i] for i in game.state.pieces(chess.ROOK, chess.WHITE)])
        rooksq = rooksq + sum([-rookstable[chess.square_mirror(i)]
                               for i in game.state.pieces(chess.ROOK, chess.BLACK)])
        queensq = sum([queenstable[i] for i in game.state.pieces(chess.QUEEN, chess.WHITE)])
        queensq = queensq + sum([-queenstable[chess.square_mirror(i)]
                                 for i in game.state.pieces(chess.QUEEN, chess.BLACK)])
        kingsq = sum([kingstable[i] for i in game.state.pieces(chess.KING, chess.WHITE)])
        kingsq = kingsq + sum([-kingstable[chess.square_mirror(i)]
                               for i in game.state.pieces(chess.KING, chess.BLACK)])

        eval = material + pawnsq + knightsq + bishopsq+ rooksq+ queensq + kingsq
        return eval