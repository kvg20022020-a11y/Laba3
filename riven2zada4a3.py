"""Recursive and iterative methods to check if a number is natural.

Provides:
- is_natural_recursive(n): Recursively checks if n is a natural number
- is_natural_iterative(n): Iterative check for comparison
- Detailed type validation and error handling
- CLI for interactive use
"""

from typing import Union, Tuple, List


def is_natural_recursive(n: Union[int, float], depth: int = 0) -> bool:
    """Check if n is a natural number using recursion.

    Natural numbers are defined as positive integers: 1, 2, 3, 4, ...
    (In some definitions, 0 is also included; we use the standard definition)

    Recursive Logic:
        Base cases:
            - If n == 1, return True (1 is natural)
            - If n <= 0, return False (not positive)
            - If n is not an integer, return False (must be whole number)
        
        Recursive case:
            - If n > 1 and is integer, check if (n-1) is natural
            - This reduces the problem: n is natural iff (n-1) is natural

    Args:
        n: Number to check (int or float)
        depth: Internal recursion depth tracking

    Returns:
        bool: True if n is a natural number, False otherwise

    Examples:
        >>> is_natural_recursive(5)
        True
        >>> is_natural_recursive(0)
        False
        >>> is_natural_recursive(5.5)
        False
        >>> is_natural_recursive(-3)
        False
    """
    # Check if n is an integer (not float unless it's a whole number)
    if isinstance(n, bool):
        return False

    if isinstance(n, float):
        # Check if float is a whole number
        if not n.is_integer():
            return False
        n = int(n)
    elif not isinstance(n, int):
        return False

    # Base case 1: n == 1 is natural
    if n == 1:
        return True

    # Base case 2: n <= 0 is not natural
    if n <= 0:
        return False

    # Recursive case: n is natural if (n-1) is natural
    return is_natural_recursive(n - 1, depth + 1)


def is_natural_iterative(n: Union[int, float]) -> bool:
    """Check if n is a natural number using iteration.

    More efficient than recursion, no risk of stack overflow.

    Args:
        n: Number to check

    Returns:
        bool: True if n is a natural number, False otherwise
    """
    # Type checking
    if isinstance(n, bool):
        return False

    if isinstance(n, float):
        if not n.is_integer():
            return False
        n = int(n)
    elif not isinstance(n, int):
        return False

    # Natural numbers are positive integers
    return n > 0


def is_natural_with_explanation(n: Union[int, float]) -> Tuple[bool, str]:
    """Check if n is natural and return explanation.

    Args:
        n: Number to check

    Returns:
        Tuple of (is_natural: bool, explanation: str)
    """
    # Type checking
    if isinstance(n, bool):
        return False, f"'{n}' є булевим значенням (bool), а не числом"

    # Check type
    if isinstance(n, float):
        if not n.is_integer():
            return False, f"{n} не є цілим числом (дробова частина: {n % 1})"
        n = int(n)
    elif isinstance(n, int):
        pass
    else:
        return False, f"'{n}' має невірний тип {type(n).__name__}"

    # Check if natural
    if n <= 0:
        if n == 0:
            reason = "0 не вважається натуральним числом"
        else:
            reason = f"{n} є від'ємним числом, натуральні числа тільки додатні"
        return False, reason
    else:
        return True, f"{n} є натуральним числом (додатне ціле число)"


def print_recursion_trace(n: int) -> None:
    """Print the recursion tree for is_natural_recursive(n).

    Args:
        n: Number to check
    """
    if not isinstance(n, int) or isinstance(n, bool) or n <= 0:
        print(f"  is_natural_recursive({n}) → False (базовий випадок)")
        return

    print(f"  Дерево рекурсії для is_natural_recursive({n}):")
    print("  " + "-" * 50)

    # Simulate recursion tree
    current = n
    depth = 0
    steps = []

    while current > 1:
        indent = "    " * depth
        steps.append(f"{indent}is_natural_recursive({current})")
        steps.append(f"{indent}  ↓ потребує: is_natural_recursive({current - 1})")
        current -= 1
        depth += 1

    # Print steps (limit for readability)
    for step in steps[:50]:
        print(f"  {step}")

    if len(steps) > 50:
        print(f"  ... (скорочено, всього {len(steps)} кроків)")

    # Base case
    print(f"  {'    ' * (n - 1)}is_natural_recursive(1)")
    print(f"  {'    ' * (n - 1)}  → True (базовий випадок)")
    print("  " + "-" * 50)


def print_check_demo(n: Union[int, float], title: str = "CHECK"):
    """Pretty print natural number check with explanation.

    Args:
        n: Number to check
        title: Title for the demonstration
    """
    print("\n" + "=" * 70)
    print(f"  {title}: Чи є {n} натуральним числом?")
    print("=" * 70)

    # Iterative check
    is_nat_iter = is_natural_iterative(n)
    print(f"  is_natural_iterative({n}) = {is_nat_iter}")

    # Recursive check (for small numbers)
    if isinstance(n, int) and 0 < n <= 20:
        is_nat_rec = is_natural_recursive(n)
        print(f"  is_natural_recursive({n}) = {is_nat_rec}")
        if is_nat_rec:
            print_recursion_trace(n)
    elif isinstance(n, (int, float)) and (isinstance(n, float) and n.is_integer() and 0 < n <= 20):
        is_nat_rec = is_natural_recursive(n)
        print(f"  is_natural_recursive({n}) = {is_nat_rec}")

    # Explanation
    result, explanation = is_natural_with_explanation(n)
    print(f"\n  Пояснення: {explanation}")
    print("=" * 70)


if __name__ == "__main__":
    print("\n" + "█" * 70)
    print("█  РЕКУРСИВНА ПЕРЕВІРКА НАТУРАЛЬНИХ ЧИСЕЛ")
    print("█" * 70)

    # Test 1: Small natural number
    print("\n[Тест 1] Натуральне число (5)")
    print_check_demo(5, "F(5)")

    # Test 2: Another natural number
    print("\n[Тест 2] Натуральне число (3)")
    print_check_demo(3, "F(3)")

    # Test 3: One (natural)
    print("\n[Тест 3] Один (базовий випадок)")
    print_check_demo(1, "F(1)")

    # Test 4: Zero (not natural)
    print("\n[Тест 4] Нуль (не натуральне)")
    print_check_demo(0, "F(0)")

    # Test 5: Negative number
    print("\n[Тест 5] Від'ємне число (-5)")
    print_check_demo(-5, "F(-5)")

    # Test 6: Float (whole)
    print("\n[Тест 6] Дробове число (цілого значення) 7.0")
    print_check_demo(7.0, "F(7.0)")

    # Test 7: Float (not whole)
    print("\n[Тест 7] Дробове число (нецілого значення) 5.5")
    print_check_demo(5.5, "F(5.5)")

    # Test 8: Float negative
    print("\n[Тест 8] Від'ємне дробове число (-3.2)")
    print_check_demo(-3.2, "F(-3.2)")

    # Test 9: Boolean
    print("\n[Тест 9] Булеве значення (True)")
    print_check_demo(True, "F(True)")

    # Test 10: String (invalid)
    print("\n[Тест 10] Рядок (невірний тип)")
    result, explanation = is_natural_with_explanation("п'ять")
    print(f"  is_natural_iterative('п'ять') → {result}")
    print(f"  Пояснення: {explanation}")

    # Test 11: Large number
    print("\n[Тест 11] Велике натуральне число (100)")
    result = is_natural_iterative(100)
    print(f"  is_natural_iterative(100) = {result}")

    # Test 12: Comparison recursive vs iterative
    print("\n[Тест 12] Порівняння рекурсивного та ітеративного методів")
    print("=" * 70)
    test_values = [0, 1, 5, 10, 15, 20, -3, 3.5, 7.0]
    print(f"  {'Число':<10} │ {'Рекурсія':<15} │ {'Ітерація':<15} │ {'Рівні?':<5}")
    print("  " + "-" * 65)

    for val in test_values:
        if isinstance(val, int) and val > 0:
            rec_result = is_natural_recursive(val)
        else:
            rec_result = is_natural_recursive(val)

        iter_result = is_natural_iterative(val)
        equal = "✓" if rec_result == iter_result else "✗"
        print(
            f"  {str(val):<10} │ {str(rec_result):<15} │ {str(iter_result):<15} │ {equal:<5}"
        )

    print("=" * 70)

    # Test 13: Type checking
    print("\n[Тест 13] Тестування типів")
    print("=" * 70)
    test_types = [
        (42, "int"),
        (42.0, "float (ціле)"),
        (42.5, "float (дробове)"),
        (True, "bool"),
        ("42", "str"),
        ((4,), "tuple"),
        ([4], "list"),
    ]

    for val, desc in test_types:
        try:
            result = is_natural_iterative(val)
            print(f"  {desc:<20} ({val!r:<10}): {result}")
        except Exception as e:
            print(f"  {desc:<20} ({val!r:<10}): Помилка - {e}")

    print("=" * 70)

    # Interactive mode
    print("\n" + "█" * 70)
    print("█  ІНТЕРАКТИВНИЙ РЕЖИМ")
    print("█" * 70)

    while True:
        print("\n1. Перевірити число (з поясненням)")
        print("2. Показати дерево рекурсії (для малих чисел)")
        print("3. Вихід")
        choice = input("\nВиберіть опцію (1-3): ").strip()

        if choice == "3":
            print("До побачення!")
            break

        if choice not in ["1", "2"]:
            print("Невірна опція.")
            continue

        print("\nВведіть число для перевірки:")
        user_input = input(">>> ").strip()

        try:
            # Try to parse as int first, then float
            try:
                if "." in user_input:
                    n_val = float(user_input)
                else:
                    n_val = int(user_input)
            except ValueError:
                raise ValueError(f"'{user_input}' не є числом")

            if choice == "1":
                print_check_demo(n_val, "ПЕРЕВІРКА")

            elif choice == "2":
                if isinstance(n_val, int) and n_val > 0 and n_val <= 15:
                    print("\n" + "=" * 70)
                    print_recursion_trace(n_val)
                    result = is_natural_recursive(n_val)
                    print(f"  Результат: {result}")
                    print("=" * 70)
                elif isinstance(n_val, float) and n_val.is_integer() and 0 < n_val <= 15:
                    print("\n" + "=" * 70)
                    print_recursion_trace(int(n_val))
                    result = is_natural_recursive(n_val)
                    print(f"  Результат: {result}")
                    print("=" * 70)
                else:
                    print("  Дерево рекурсії показується тільки для натуральних чисел від 1 до 15")

        except ValueError as e:
            print(f"✗ Помилка: {e}")
        except Exception as e:
            print(f"✗ Невідома помилка: {e}")

    # Summary info
    print("\n" + "=" * 70)
    print("  ІНФОРМАЦІЯ ПРО НАТУРАЛЬНІ ЧИСЛА")
    print("=" * 70)
    print("""
  Натуральні числа - це множина додатних цілих чисел.

  Визначення:
    ℕ = {1, 2, 3, 4, 5, 6, ...}
  
  Дуже важливо: У багатьох定義 до натуральних чисел входить 0:
    ℕ₀ = {0, 1, 2, 3, 4, 5, ...}
  
  У цій програмі використовується стандартне визначення без нуля.

  Властивості натуральних чисел:
    • Всі натуральні числа - це цілі числа
    • Всі натуральні числа - додатні (> 0)
    • Натуральні числа можна складати: a + b ∈ ℕ
    • Натуральні числа можна множити: a × b ∈ ℕ

  Рекурсивна перевірка:
    - Базовий випадок: 1 є натуральним
    - Рекурсивний випадок: n є натуральним, якщо (n-1) є натуральним
    - Часова складність: O(n)
    - Просторова складність: O(n) - стек викликів
    - УВАГА: Небезпечна для великих чисел (переповнення стека)

  Ітеративна перевірка:
    - Просто перевіримо: n > 0 та n є цілим числом
    - Часова складність: O(1)
    - Просторова складність: O(1)
    - РЕКОМЕНДУЄТЬСЯ в практиці

  Що НЕ є натуральним числом:
    • 0 (за стандартним визначенням)
    • Від'ємні числа (-1, -5, -100, ...)
    • Дробові числа (1.5, 3.14, 0.001, ...)
    • Комплексні числа (1+2i, ...)
    • Нецислові типи (рядки, списки, об'єкти, ...)
    """)
    print("=" * 70)
