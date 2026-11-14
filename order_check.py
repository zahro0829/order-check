# Модуль 1: Проверка порядка. Элементы передаются
# в процедуру по одному (через *letters).
def check_order(*letters) -> bool:
    """Проверяет, расположены ли строчные латинские буквы
    в алфавитном порядке. Пустой массив считается
    упорядоченным (явное решение)."""
    if not letters:
        return True
    for ch in letters:
        if not (isinstance(ch, str) and len(ch) == 1
                and 'a' <= ch <= 'z'):
            raise TypeError(f"Недопустимый элемент: {ch!r}")
    return all(a <= b for a, b in zip(letters, letters[1:]))

# Модуль 2: Обработка одного массива
def process_array(number: int, *letters: str) -> str:
    """Возвращает номер массива, если буквы упорядочены,
    иначе "нет" """
    return str(number) if check_order(*letters) else "нет"

# Модуль 3: Главный модуль — сборка отчёта
def print_report(arrays) -> None:
    """Печатает результат проверки для каждого массива."""
    for number, arr in enumerate(arrays, start=1):
        try:
            print(f"Массив {number}: {process_array(number, *arr)}")
        except TypeError as e:
            print(f"Массив {number}: ошибка данных ({e})")

if __name__ == "__main__":
    print_report([
        ['a', 'b', 'c', 'd'],
        ['b', 'a', 'c'],
        ['a', 'a', 'b'],
        ['m', 'n', 'p', 'o'],
        ['a', 'b', 'z'],
    ])
