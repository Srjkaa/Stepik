# Напишите простой калькулятор, который считывает с пользовательского ввода три
# строки: первое число, второе число и операцию, после чего применяет операцию
# к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.
# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.
# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
# Обратите внимание, что на вход программе приходят вещественные числа.


def simple_calc(num1, num2, operation):
    if operation == '+':
        print(num1 + num2)
    elif operation == '-':
        print(num1 - num2)
    elif operation == '/':
        print(num1 / num2 if num2 != 0 else 'Деление на 0!')
    elif operation == '*':
        print(num1 * num2)
    elif operation == 'mod':
        print(num1 % num2 if num2 != 0 else 'Деление на 0!')
    elif operation == 'pow':
        print(num1 ** num2)
    elif operation == 'div':
        print(num1 // num2 if num2 != 0 else 'Деление на 0!')


if __name__ == '__main__':
    num1, num2 = (float(input()) for _ in range(2))
    operation = input()
    simple_calc(num1, num2, operation)
