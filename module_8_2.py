def personal_sum(numbers):
    incorrect_data = 0
    result = 0
    for i in range(len(numbers)):
        try:
            result += numbers[i]
        except TypeError:
             print(f'Некорректный тип данных для подсчёта суммы: {numbers[i]}')
             incorrect_data += 1
    return (result, incorrect_data)


def calculate_average(numbers):
    ar_mean = 0
    try:
        summ = personal_sum(numbers)
        ar_mean = summ[0] / len(numbers)
    except ZeroDivisionError:
        ar_mean = 0
    except TypeError:
         print('В numbers записан некорректный тип данных')
    finally:
        return ar_mean


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')