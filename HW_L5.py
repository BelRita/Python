# 1

with open('Doc.txt', 'w') as f:
    while True:
        new_data = input('New line: ')
        if new_data == '':
            break
        f.write(new_data + '\n')

# 2

with open('Doc1.txt') as d:
    lines = d.readlines()
print('Quantity of lines: ', len(lines))
for num_line, line in enumerate(lines, start=1):
    print('{} line has - {} words'.format(num_line, len(line.split())))

# 3

with open('Doc2.txt', encoding='utf-8') as b:
    lines = b.readlines()
salaries = []
for line in lines:
    name, salary = line.split(' ')
    salaries.append(int(salary))
    if int(salary) < 20000:
        print(line, end='')
print('\nСредняя зп:', sum(salaries) / len(salaries))
print(salaries)

# 4

with open('Doc3.txt', encoding='utf-8') as f:
    lines = f.readlines()
with open('rus.txt', 'w', encoding='utf-8') as f:
    for line in lines:
        if '1' in line:
            line = line.replace('One', 'Один')
        elif '2' in line:
            line = line.replace('Two', 'Два')
        elif '3' in line:
            line = line.replace('Three', 'Три')
        elif '4' in line:
            line = line.replace('Four', 'Четыре')
        f.write(line)

5

with open('Doc4.txt', 'w', encoding='utf-8') as f:
    nums = input('Введите целые числа через пробел: ')
    f.write('Введенные числа: ' + nums + '\n')
    nums = map(int, nums.split())
    sum_nums = sum(nums)
    f.write('Сумма чисел: ' + str(sum_nums))
    print('Сумма введенных чисел:', sum_nums)
print('Все записано в файл')

# 6

my_dict = dict()
with open('Doc5.txt', encoding='utf-8') as f:
    lines = f.readlines()
for line in lines:
    splitted_line = line.split()
    subject = splitted_line[0]
    print(splitted_line)
    sum_lessons = sum([int(x[:x.find('(')]) for x in splitted_line[1:] if '(' in x])
    my_dict[subject[:-1]] = sum_lessons
print(my_dict)

# 7

import json

firm_dict = {}
average_profit = []
with open('Doc6.txt', encoding='utf-8') as f:
    lines = f.readlines()

for line in lines:
    name, form, revenue, costs = line.split()
    profit = int(revenue) - int(costs)
    firm_dict[name] = profit
    if profit > 0:
        average_profit.append(profit)
average_profit = sum(average_profit) / len(average_profit)
out_info = [firm_dict, {'average_profit': average_profit}]

with open('Doc6.txt.json', 'w') as f_json:
    json.dump(out_info, f_json)

with open('Doc6.txt.json') as f_json:
    print(json.load(f_json))