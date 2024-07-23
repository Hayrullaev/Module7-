team1_num = 5
team2_num = 6
team1_time = 18015.2
score_1 = 40
score_2 = 42
challenge_result = "победа команды Мастера кода!"
tasks_total = 82
time_avg = 350.4

# Использование %-форматирования:
print("В команде Мастера кода участников: " + str(team1_num) + " !")
print("Итого сегодня в командах участников: " + str(team1_num) + " и " + str(team2_num) + " !")

# Использование format():
print("Команда Волшебники данных решила задач: {} !".format(score_2))
print("Волшебники данных решили задачи за {:.2f} с !".format(team1_time))

# Использование f-строк:
print(f"В команде Мастера кода участников: {team1_num} !")
print(f"Итого сегодня в командах участников: {team1_num} и {team2_num} !")
print(f"Команда Волшебники данных решила задач: {score_2} !")
print(f"Волшебники данных решили задачи за {team1_time} с !")


print("Команды решили", score_1, "и", score_2, "задач.")
print(f"Результат битвы: {challenge_result}")
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.2f} секунды на задачу!")