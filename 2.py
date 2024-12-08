# TODO Напишите функцию find_common_participants
def  find_common_participants (first,second, i =','):
    firstgroup = set(first.split(i))
    secondgroup = set(second.split(i))
    common_participants = firstgroup.intersection(secondgroup)
    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
