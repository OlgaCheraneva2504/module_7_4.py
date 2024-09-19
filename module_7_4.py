team1 = 'Мастера кода'
team2 = 'Волшебники данных'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.51
team2_time = 2153.31
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = f'Победа команды {team1}!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = f'Победа команды {team2}!'
else:
    challenge_result = 'Ничья!'

# Использовние %:
print('В команде %s участников: %s!' % (team1, team1_num))
print('Итого сегодгя в командах участников: %s и %s!' % (team1_num, team2_num))

# Использовние format():
print('Команда {} решила задач: {}!'.format(team2, score_2))
print('{} решили задачи за {} с!'.format(team2, team2_time))

# Использовние f-строк:
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат быитвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.2f} секунды на задачу!')