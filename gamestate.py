xAxis, yAxis = 3, 2


class GameState:

    def __init__(self):
        self._board = [[0] * yAxis for _ in range(xAxis)]
        self._board[-1][-1] = 1
        self._activePlayer = 0
        self._player_locations = [None, None]


if __name__ == '__main__':
    gameState = GameState()
