# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"
ensure_ascii = True

def task() -> None:
    with open(INPUT_FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        space = []
        for i in reader:
            data.append(i)

    with open(OUTPUT_FILENAME, 'w') as file:
        json.dump(space, file, indent=4, ensure_ascii=ensure_ascii)


 # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")