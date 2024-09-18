first_team_name = 'Мастера кода'
second_team_name = 'Волшебники данных'
first_team_count = 5
second_team_count = 6
first_team_time = 1552.512
second_team_time = 2153.31451
first_team_tasks = 40
second_team_tasks = 42
tasks_total = first_team_tasks + second_team_tasks
time_total = first_team_time + second_team_time
time_avg = time_total / tasks_total

if first_team_tasks > second_team_tasks or first_team_tasks == second_team_tasks and first_team_time > second_team_time:
    result = 'Победа команды Мастера кода!'
elif first_team_tasks < second_team_tasks or first_team_tasks == second_team_tasks and first_team_time < second_team_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'

# %
print('В команде %(name)s участников: %(count)x' % {'name': first_team_name, 'count': first_team_count})
print(
    'Итого сегодня в командах участников: %(first)x и %(second)x !' % {
        'first': first_team_count,
        'second': second_team_count
    }
)

# format()
print('Команда {} решила: {} задач'.format(second_team_name, second_team_tasks))
print('{} решили задачи за {} c !'.format(second_team_name, second_team_time))

# f-строки
print(f'Команды решили {first_team_tasks} и {second_team_tasks} задач.')
print(f'Результаты битвы: {result}')
