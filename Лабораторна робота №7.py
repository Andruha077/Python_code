# Введення кількості очок, набраних кожною з 9 команд
scores = []
for i in range(9):
    score = int(input(f"Введіть кількість очок, набраних командою {i + 1}: "))
    scores.append(score)

# Введення кількості очок, набраних новою командою
new_team_score = int(input("Введіть кількість очок, набраних новою командою: "))

# Визначення місця, яке зайняла нова команда
rank = sum(score > new_team_score for score in scores) + 1

# Визначення назв команд, які набрали менше очок, ніж нова команда
weaker_teams = [i + 1 for i, score in enumerate(scores) if score < new_team_score]

# Виведення результатів
print(f"Нова команда зайняла {rank}-е місце.")
print(f"Команди, які набрали менше очок, ніж нова команда:", weaker_teams)