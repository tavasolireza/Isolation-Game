from copy import deepcopy

xAxis, yAxis = 3, 2


class GameState:

    def __init__(self):
        self._board = [[0] * yAxis for _ in range(xAxis)]
        self._board[-1][-1] = 1
        self._activePlayer = 0
        self._player_locations = [None, None]

    def forecast_move(self, move):
        if move not in self.get_legal_moves():
            raise RuntimeError("Attempted forecast of illegal move")
        new_board = deepcopy(self)
        new_board._board[move[0]][move[1]] = 1
        new_board._player_locations[self._activePlayer] = move
        new_board._activePlayer ^= 1
        return new_board

    def get_legal_moves(self):
        location = self._player_locations[self._activePlayer]
        if location is not None:
            return self._get_blank_spaces()
        moves = []
        all_moves = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
        for x_move, y_move in all_moves:
            _x, _y = location
            while (_x in range(0, xAxis)) and (_y in range(0, yAxis)):
                _x, _y = _x + x_move, _y + y_move
                if self._board[_x][_y] == 1:
                    break
                moves.append((_x, _y))
        return moves

    def _get_blank_spaces(self):
        return [(x, y) for y in range(yAxis) for x in range(xAxis) if self._board[x][y] == 0]


if __name__ == '__main__':
    gameState = GameState()
