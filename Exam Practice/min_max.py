import math

# Minimax function
def minimax(depth, node_index, maximizing_player, values, alpha, beta):
    # Base case: Leaf node
    if depth == 3:
        return values[node_index]

    if maximizing_player:
        best = -math.inf
        for i in range(2):  # Two children
            val = minimax(depth + 1, node_index * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break  # Alpha-beta pruning
        return best
    else:
        best = math.inf
        for i in range(2):  # Two children
            val = minimax(depth + 1, node_index * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break  # Alpha-beta pruning
        return best

# Example tree leaf values
values = [3, 5, 2, 9, 0, 7, 4, 6]

# Call minimax (root node)
best_move = minimax(0, 0, True, values, -math.inf, math.inf)
print("Best move value:", best_move)
