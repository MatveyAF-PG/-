# TODO решите задачу
import json

name = 'input.json'
with open(name) as file:
    s = json.load(file)

def task(json) -> float:
    summa= 0
    for i in json:
        summa += float(i["weight"]) * float(i["score"])
    return summa

print(f'{task(s):.3f}')