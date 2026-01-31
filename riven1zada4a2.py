"""Function to sum arbitrary number of arguments with validation.

This module provides a flexible sum function that accepts any number of arguments
and validates that all arguments are numeric.
"""

from typing import Union


def calculate_sum(*args: Union[int, float]) -> Union[int, float]:
    """Calculate the sum of arbitrary number of numeric arguments.
    
    Validates that all arguments are numeric (int or float).
    Raises TypeError if any argument is not a number.
    
    Args:
        *args: Arbitrary number of numeric arguments (int or float)
        
    Returns:
        Union[int, float]: The sum of all arguments. Returns 0 if no arguments.
        
    Raises:
        TypeError: If any argument is not a number (int or float)
        
    Examples:
        >>> calculate_sum(1, 2, 3)
        6
        >>> calculate_sum(1.5, 2.5, 3)
        7.0
        >>> calculate_sum()
        0
        >>> calculate_sum(1, "2")  # Raises TypeError
    """
    # Check if no arguments provided
    if len(args) == 0:
        return 0
    
    # Validate all arguments are numeric
    for arg in args:
        if not isinstance(arg, (int, float)) or isinstance(arg, bool):
            raise TypeError(
                f"Argument '{arg}' has invalid type {type(arg).__name__}. "
                f"Only int or float are allowed."
            )
    
    # Calculate and return the sum
    return sum(args)


def calculate_sum_safe(*args) -> Union[int, float, str]:
    """Calculate sum with graceful error handling (returns error message).
    
    Similar to calculate_sum but returns error message instead of raising exception.
    
    Args:
        *args: Arbitrary number of arguments
        
    Returns:
        Union[int, float, str]: The sum or an error message
    """
    if len(args) == 0:
        return 0
    
    for arg in args:
        if not isinstance(arg, (int, float)) or isinstance(arg, bool):
            return f"Помилка: '{arg}' не є числом (тип: {type(arg).__name__})"
    
    return sum(args)


if __name__ == "__main__":
    print("=" * 60)
    print("ФУНКЦІЯ ДЛЯ ОБЧИСЛЕННЯ СУМИ ДОВІЛЬНОЇ КІЛЬКОСТІ ЧИСЕЛ")
    print("=" * 60)
    
    # Test 1: Normal usage with integers
    print("\n[Тест 1] Сума цілих чисел:")
    try:
        result = calculate_sum(1, 2, 3, 4, 5)
        print(f"  calculate_sum(1, 2, 3, 4, 5) = {result}")
    except TypeError as e:
        print(f"  Помилка: {e}")
    
    # Test 2: Normal usage with floats
    print("\n[Тест 2] Сума дробових чисел:")
    try:
        result = calculate_sum(1.5, 2.5, 3.0)
        print(f"  calculate_sum(1.5, 2.5, 3.0) = {result}")
    except TypeError as e:
        print(f"  Помилка: {e}")
    
    # Test 3: Mixed integers and floats
    print("\n[Тест 3] Сума цілих і дробових чисел:")
    try:
        result = calculate_sum(10, 5.5, 2, 1.25)
        print(f"  calculate_sum(10, 5.5, 2, 1.25) = {result}")
    except TypeError as e:
        print(f"  Помилка: {e}")
    
    # Test 4: No arguments
    print("\n[Тест 4] Без аргументів:")
    try:
        result = calculate_sum()
        print(f"  calculate_sum() = {result}")
    except TypeError as e:
        print(f"  Помилка: {e}")
    
    # Test 5: Negative numbers
    print("\n[Тест 5] З від'ємними числами:")
    try:
        result = calculate_sum(-5, 10, -3.5, 2)
        print(f"  calculate_sum(-5, 10, -3.5, 2) = {result}")
    except TypeError as e:
        print(f"  Помилка: {e}")
    
    # Test 6: Invalid input - string
    print("\n[Тест 6] Невірний ввід (рядок):")
    try:
        result = calculate_sum(1, 2, "три")
        print(f"  calculate_sum(1, 2, 'три') = {result}")
    except TypeError as e:
        print(f"  ✗ Помилка: {e}")
    
    # Test 7: Invalid input - boolean
    print("\n[Тест 7] Невірний ввід (булево значення):")
    try:
        result = calculate_sum(1, 2, True)
        print(f"  calculate_sum(1, 2, True) = {result}")
    except TypeError as e:
        print(f"  ✗ Помилка: {e}")
    
    # Test 8: Invalid input - list
    print("\n[Тест 8] Невірний ввід (список):")
    try:
        result = calculate_sum(1, 2, [3, 4])
        print(f"  calculate_sum(1, 2, [3, 4]) = {result}")
    except TypeError as e:
        print(f"  ✗ Помилка: {e}")
    
    # Test 9: Using safe version with invalid input
    print("\n[Тест 9] Безпечна версія з помилкою:")
    result = calculate_sum_safe(5, 10, "невалідно", 3)
    print(f"  calculate_sum_safe(5, 10, 'невалідно', 3) = {result}")
    
    # Test 10: Interactive user input
    print("\n" + "=" * 60)
    print("ІНТЕРАКТИВНИЙ РЕЖИМ")
    print("=" * 60)
    
    while True:
        print("\nВведіть числа для сумування (розділені пробілом) або 'вихід' для завершення:")
        user_input = input(">>> ").strip()
        
        if user_input.lower() in ['вихід', 'exit', 'quit']:
            print("До побачення!")
            break
        
        try:
            # Parse input
            numbers = []
            for token in user_input.split():
                try:
                    # Try to convert to int first, then float
                    if '.' in token:
                        numbers.append(float(token))
                    else:
                        numbers.append(int(token))
                except ValueError:
                    raise ValueError(f"'{token}' не є числом")
            
            # Calculate sum
            if numbers:
                result = calculate_sum(*numbers)
                print(f"✓ Сума: {result}")
            else:
                print("Помилка: не було введено жодного числа")
                
        except ValueError as e:
            print(f"✗ Помилка: {e}")
        except TypeError as e:
            print(f"✗ Помилка: {e}")
