def game_score(actions):
    points = {'win': 3, 'draw': 1, 'lose': 0}
    return sum(points.get(action, 0) for action in actions)

print(f"Тест 1: {game_score(['win', 'draw', 'lose', 'win'])}")
print(f"Тест 2: {game_score(['win', 'win', 'win'])}")
print(f"Тест 3: {game_score(['lose', 'lose', 'draw'])}")