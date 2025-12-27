import re
from typing import Callable, Generator

def generator_numbers(text: str):
    """
    Функція-генератор для виділення дійсних чисел у тексті.

    :param text: рядок з текстом, який містить дійсні числа
    :return: генератор чисел float, які знайдені в тексті
    """
     
    pattern = r"\b\d+(?:\.\d+)?\b" # шукає числа з десятковою точкою
    for match in re.findall(pattern, text):
        yield float(match)

def sum_profit(text: str, 
        func: Callable[[str], 
        Generator[float, None, None]]):
    """
    Обчислює загальний дохід, підсумовуючи всі числа, знайдені в тексті.

    Використовує генератор чисел, що повертає функція func.

    :param text: Рядок з числами (доходами)
    :param func: Функція-генератор чисел (наприклад, generator_numbers)
    :return: Загальна сума чисел
    """
    total = 0.0
    for number in func(text):
        total += number
    return total


text = "Загальний дохід працівника складається з декількох частин: " \
"1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і " \
"324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
