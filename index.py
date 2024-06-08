import bz2
file_path = '10m.txt.bz2'

#Максимальне число в файлі
def find_max_number(file_path):
    max_number = None
    with bz2.open(file_path, 'rt') as file:
        for line in file:
            number = int(line.strip())
            if max_number is None or number > max_number:
                max_number = number
    return max_number
max_number = find_max_number(file_path)
print("Максимальне число в файлі:", max_number)


#Мінімальне число в файлі
def find_min_number(file_path):
    min_number = None
    with bz2.open(file_path, 'rt') as file:
        for line in file:
            number = int(line.strip())
            if min_number is None or number < min_number:
                min_number = number
    return min_number

min_number = find_min_number(file_path)
print("Мінімальне число в файлі:", min_number)

#Медіану
def find_median(file_path):
    numbers = []
    with bz2.open(file_path, 'rt') as file:
        for line in file:
            numbers.append(int(line.strip()))
    
    numbers.sort()
    n = len(numbers)
    if n % 2 == 1:
        median = numbers[n // 2]
    else:
        median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2
    
    return median

median = find_median(file_path)
print("Медіана в файлі:", median)

#Середнє арифметичне значення
def find_mean(file_path):
    total = 0
    count = 0
    with bz2.open(file_path, 'rt') as file:
        for line in file:
            total += int(line.strip())
            count += 1
    
    if count == 0:
        return 0  # уникнення ділення на нуль
    else:
        return total / count

mean = find_mean(file_path)
print("Середнє арифметичне значення в файлі:", mean)

#Найбільшу послідовність чисел (які ідуть один за одним), яка збільшується (опціонально)
def find_longest_increasing_sequence(file_path):
    longest_sequence = []
    current_sequence = []
    previous_number = None

    with bz2.open(file_path, 'rt') as file:
        for line in file:
            number = int(line.strip())
            if previous_number is None or number > previous_number:
                current_sequence.append(number)
            else:
                if len(current_sequence) > len(longest_sequence):
                    longest_sequence = current_sequence
                current_sequence = [number]
            previous_number = number

    # Перевіряємо останню поточну послідовність
    if len(current_sequence) > len(longest_sequence):
        longest_sequence = current_sequence

    return longest_sequence

longest_sequence = find_longest_increasing_sequence(file_path)
print("Найдовша зростаюча послідовність чисел:", longest_sequence)


#Найбільшу послідовність чисел (які ідуть один за одним), яка зменшується (опціонально)

def find_longest_decreasing_sequence(file_path):
    longest_sequence = []
    current_sequence = []
    previous_number = None

    with bz2.open(file_path, 'rt') as file:
        for line in file:
            number = int(line.strip())
            if previous_number is None or number < previous_number:
                current_sequence.append(number)
            else:
                if len(current_sequence) > len(longest_sequence):
                    longest_sequence = current_sequence
                current_sequence = [number]
            previous_number = number

    # Перевіряємо останню поточну послідовність
    if len(current_sequence) > len(longest_sequence):
        longest_sequence = current_sequence

    return longest_sequence

longest_sequence = find_longest_decreasing_sequence(file_path)
print("Найдовша зменшуюча послідовність чисел:", longest_sequence)