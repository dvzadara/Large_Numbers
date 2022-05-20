from math import *
import random
import time


# Перебирает все ключи в заданом диапазоне [0, key_range) пока не не будет найдено значение равное key
# Возвращает время в мс
def broodforce(key_range: int, key: int):
    start_time = time.time()
    for k in range(key_range):
        if k == key:
            print(f"Найден ключ: {k}")
            return round((time.time() - start_time) * 1000)


if __name__ == "__main__":
    key_sizes = [2 ** x for x in range(int(log2(8)), int(log2(4096)) + 1)]
    for key_size in key_sizes:
        key_range = 2 ** key_size
        print(f"Количество вариантов {key_size}-битных ключей: {key_range}")

    for key_size in key_sizes:
        key_range = 2 ** key_size
        key = random.randint(0, key_range - 1)
        print(f"Случайный {key_size}-битный ключ: {key}")
        print(f"Время перебора: {broodforce(key_range, key)} мс")
