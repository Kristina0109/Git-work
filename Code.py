import sympy as sp

def calculate_derivative():
    # Ввод данных
    function_input = input("Введите функцию f(x): ")
    x_value = float(input("Введите значение x: "))

    # Предобработка данных
    x = sp.symbols('x')
    try:
        function = sp.sympify(function_input)
    except sp.SympifyError:
        print("Ошибка: неверный ввод функции.")
        return

    # Расчёт производной
    derivative = sp.diff(function, x)

    # Вычисление значения производной
    derivative_value = derivative.evalf(subs={x: x_value})

    # Вывод результата
    print(f"Производная: {derivative}")
    print(f"Значение производной в точке x={x_value}: {derivative_value}")

# Запуск программы
calculate_derivative()
