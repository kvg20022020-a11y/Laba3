"""Function to build a table (dictionary) of values for any function and input values.

This module provides utilities to apply a function to multiple input values
and create a dictionary (table) of results.
"""

from typing import Callable, Dict, List, Any, Union, Iterable
import math


def build_table(func: Callable, values: Iterable, 
                handle_errors: bool = True) -> Dict[Any, Any]:
    """Build a dictionary (table) of function values.
    
    Applies a given function to each input value and creates a dictionary
    with input values as keys and function results as values.
    
    Args:
        func: A callable function to apply to each value
        values: An iterable of input values (list, tuple, range, etc.)
        handle_errors: If True, stores error message instead of raising exception
                      If False, propagates exceptions
        
    Returns:
        Dict[Any, Any]: A dictionary mapping input values to function results.
                       If handle_errors=True, failed values map to error messages.
        
    Examples:
        >>> build_table(lambda x: x**2, [1, 2, 3, 4, 5])
        {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
        
        >>> build_table(math.sqrt, [1, 4, 9, 16])
        {1: 1.0, 4: 2.0, 9: 3.0, 16: 4.0}
        
        >>> build_table(lambda x: 1/x, [1, 0, 2], handle_errors=True)
        {1: 1.0, 0: 'ZeroDivisionError: division by zero', 2: 0.5}
    """
    result = {}
    
    # Convert values to list if needed
    values_list = list(values)
    
    if len(values_list) == 0:
        return result
    
    # Check if func is callable
    if not callable(func):
        raise TypeError(f"First argument must be callable, got {type(func).__name__}")
    
    # Build the table
    for value in values_list:
        try:
            result[value] = func(value)
        except Exception as e:
            if handle_errors:
                error_name = type(e).__name__
                error_msg = str(e)
                result[value] = f"{error_name}: {error_msg}"
            else:
                raise
    
    return result


def build_table_with_validation(func: Callable, values: Iterable,
                               input_validator: Callable[[Any], bool] = None,
                               skip_invalid: bool = False) -> Dict[Any, Any]:
    """Build a table with optional input validation.
    
    Args:
        func: Function to apply
        values: Iterable of input values
        input_validator: Optional function to validate each input.
                        Should return True if valid, False if invalid.
        skip_invalid: If True, skip invalid values. If False, include them
                     in result with error message.
        
    Returns:
        Dict[Any, Any]: Table of function results
    """
    result = {}
    values_list = list(values)
    
    if not callable(func):
        raise TypeError(f"func must be callable")
    
    for value in values_list:
        # Check validation if provided
        if input_validator is not None:
            try:
                if not input_validator(value):
                    if skip_invalid:
                        continue
                    else:
                        result[value] = f"Validation failed: {value} is invalid"
                        continue
            except Exception as e:
                result[value] = f"Validation error: {e}"
                continue
        
        # Apply function
        try:
            result[value] = func(value)
        except Exception as e:
            error_name = type(e).__name__
            result[value] = f"{error_name}: {str(e)}"
    
    return result


def print_table(table: Dict[Any, Any], title: str = "TABLE") -> None:
    """Pretty print a function table.
    
    Args:
        table: Dictionary to print
        title: Title for the table
    """
    if not table:
        print("(empty table)")
        return
    
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)
    
    # Find max widths for formatting
    max_key_width = max(len(str(k)) for k in table.keys())
    max_val_width = max(len(str(v)) for v in table.values())
    
    max_key_width = max(max_key_width, 5)
    max_val_width = max(max_val_width, 7)
    
    # Print header
    print(f"  {'Input':<{max_key_width}} │ {'Output':<{max_val_width}}")
    print("  " + "-" * (max_key_width + max_val_width + 3))
    
    # Print rows
    for key, value in table.items():
        print(f"  {str(key):<{max_key_width}} │ {str(value):<{max_val_width}}")
    
    print("=" * 70)


if __name__ == "__main__":
    print("\n" + "█" * 70)
    print("█  ФУНКЦІЯ ДЛЯ ПОБУДОВИ ТАБЛИЦІ ЗНАЧЕНЬ")
    print("█" * 70)
    
    # Test 1: Square function
    print("\n[Тест 1] Функція f(x) = x²")
    table1 = build_table(lambda x: x**2, [1, 2, 3, 4, 5])
    print_table(table1, "Квадрати чисел")
    
    # Test 2: Square root function
    print("\n[Тест 2] Функція f(x) = √x")
    table2 = build_table(math.sqrt, [1, 4, 9, 16, 25, -1])
    print_table(table2, "Квадратні корені")
    
    # Test 3: Reciprocal function (with error handling)
    print("\n[Тест 3] Функція f(x) = 1/x (з обробкою помилок)")
    table3 = build_table(lambda x: 1/x, [1, 0, 2, -2, 0.5], handle_errors=True)
    print_table(table3, "Обернені числа")
    
    # Test 4: Trigonometric function
    print("\n[Тест 4] Функція f(x) = sin(x)")
    table4 = build_table(math.sin, [0, math.pi/6, math.pi/4, math.pi/3, math.pi/2])
    print_table(table4, "Синус кутів")
    
    # Test 5: Custom function
    print("\n[Тест 5] Функція f(x) = 2x + 3")
    def linear(x):
        return 2*x + 3
    table5 = build_table(linear, range(-2, 4))
    print_table(table5, "Лінійна функція")
    
    # Test 6: String operations
    print("\n[Тест 6] Функція f(s) = len(s) (довжина рядка)")
    words = ["Python", "функція", "таблиця", "а", "програмування"]
    table6 = build_table(len, words, handle_errors=True)
    print_table(table6, "Довжини слів")
    
    # Test 7: With validation
    print("\n[Тест 7] З валідацією (тільки додатні числа)")
    def is_positive(x):
        return isinstance(x, (int, float)) and x > 0
    
    values_mixed = [1, -2, 3, -4, 5, 0]
    table7 = build_table_with_validation(
        lambda x: x**2,
        values_mixed,
        input_validator=is_positive,
        skip_invalid=False
    )
    print_table(table7, "Квадрати з валідацією")
    
    # Test 8: Logarithm (positive numbers only)
    print("\n[Тест 8] Функція f(x) = ln(x) (лог. натуральний)")
    values_log = [1, 2.718, 10, 100, 0, -5]
    table8 = build_table(math.log, values_log, handle_errors=True)
    print_table(table8, "Натуральні логарифми")
    
    # Test 9: Lambda with multiple operations
    print("\n[Тест 9] Функція f(x) = x³ - 2x + 1")
    table9 = build_table(lambda x: x**3 - 2*x + 1, [-2, -1, 0, 1, 2])
    print_table(table9, "Поліном третього степеня")
    
    # Test 10: Factorial (integers only)
    print("\n[Тест 10] Функція f(x) = x! (факторіал)")
    table10 = build_table(math.factorial, [0, 1, 2, 3, 4, 5, -1], handle_errors=True)
    print_table(table10, "Факторіали")
    
    # Interactive mode
    print("\n" + "█" * 70)
    print("█  ІНТЕРАКТИВНИЙ РЕЖИМ")
    print("█" * 70)
    
    while True:
        print("\n1. Побудувати таблицю по готовій функції")
        print("2. Задати власну функцію (у форматі Python)")
        print("3. Вихід")
        choice = input("\nВиберіть опцію (1-3): ").strip()
        
        if choice == "3":
            print("До побачення!")
            break
        
        if choice not in ["1", "2"]:
            print("Невірна опція.")
            continue
        
        # Get values from user
        print("\nВведіть значення для обчислення (розділені пробілом):")
        values_input = input(">>> ").strip()
        
        try:
            values = []
            for val in values_input.split():
                try:
                    if '.' in val:
                        values.append(float(val))
                    else:
                        values.append(int(val))
                except ValueError:
                    raise ValueError(f"'{val}' не є числом")
            
            if not values:
                print("Помилка: не введено жодного числа")
                continue
            
            if choice == "1":
                print("\nДоступні функції:")
                print("  1. x²          (square)")
                print("  2. √x          (sqrt)")
                print("  3. sin(x)      (sin)")
                print("  4. cos(x)      (cos)")
                print("  5. ln(x)       (log)")
                print("  6. eˣ          (exp)")
                print("  7. 1/x         (reciprocal)")
                
                func_choice = input("\nВиберіть функцію (1-7): ").strip()
                
                functions = {
                    "1": (lambda x: x**2, "Квадрат"),
                    "2": (math.sqrt, "Квадратний корінь"),
                    "3": (math.sin, "Синус"),
                    "4": (math.cos, "Косинус"),
                    "5": (math.log, "Натуральний логарифм"),
                    "6": (math.exp, "Експонента"),
                    "7": (lambda x: 1/x, "Обернене число"),
                }
                
                if func_choice not in functions:
                    print("Невірна функція")
                    continue
                
                func, func_name = functions[func_choice]
                result = build_table(func, values, handle_errors=True)
                print_table(result, func_name)
            
            elif choice == "2":
                print("\nВведіть функцію у форматі Python (змінна: x):")
                print("Приклади: x**2, x*2+3, 1/x, math.sqrt(x)")
                func_str = input(">>> ").strip()
                
                # Create function
                def user_func(x):
                    return eval(func_str, {"x": x, "math": math})
                
                result = build_table(user_func, values, handle_errors=True)
                print_table(result, f"f(x) = {func_str}")
        
        except Exception as e:
            print(f"✗ Помилка: {e}")
