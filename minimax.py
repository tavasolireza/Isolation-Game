def terminal_test(gameState):
    terminal_state = bool(gameState.get_legal_moves())
    return not terminal_state


def min_value(gameState):
    if terminal_test(gameState):
        return 1
    value = float("inf")
    for m in gameState.get_legal_moves():
        value = min(value, max_value(gameState.forecast_move(m)))
    return value


def max_value(gameState):
    if terminal_test(gameState):
        return -1
    value = float("-inf")
    for m in gameState.get_legal_moves():
        value = max(value, min_value(gameState.forecast_move(m)))
    return value
