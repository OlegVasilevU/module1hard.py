# Дополнительное практическое задание по модулю: "Базовые структуры данных."
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# Вычисляем среднию оценку каждого ученика сопоставив оценки и записываем его в список
average_grades = [sum(grades[0]) / len(grades[0]),
                   sum(grades[1]) / len(grades[1]),
                   sum(grades[2]) / len(grades[2]),
                   sum(grades[3]) / len(grades[3]),
                   sum(grades[4]) / len(grades[4])]
# Создаем словарь средней
list_average = {'Aeron':average_grades[0],
              'Bilbo':average_grades[1],
              'Johnny':average_grades[2],
              'Khendrik':average_grades[3],
              'Steve':average_grades[4]}
# выводим словарь в консоль
print(list_average)
#
