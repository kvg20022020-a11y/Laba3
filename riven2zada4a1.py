"""Recursive factorial calculation with detailed recursion visualization.

Provides:
- factorial_recursive(n): Recursive implementation of n! with memoization option
- factorial_with_steps(n): Shows the recursion tree and call sequence
- CLI for interactive use with examples
"""

from typing import Dict, List, Tuple
import sys


def factorial_recursive(n: int, memo: Dict[int, int] = None) -> int:
    """Calculate n! recursively.

    Base cases:
        0! = 1
        1! = 1

    Recursive case:
        n! = n * (n-1)!

    Args:
        n: Non-negative integer
        memo: Memoization dictionary (for optimization, internal use)

    Returns:
        int: The factorial of n

    Raises:
        TypeError: If n is not an integer
        ValueError: If n is negative
    """
    # Input validation
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"n must be an integer, got {type(n).__name__}")
    if n < 0:
        raise ValueError(f"n must be non-negative, got {n}")

    # Initialize memoization dictionary
    if memo is None:
        memo = {}

    # Check if already computed
    if n in memo:
        return memo[n]

    # Base cases
    if n == 0 or n == 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    result = n * factorial_recursive(n - 1, memo)
    memo[n] = result
    return result


def factorial_iterative(n: int) -> int:
    """Calculate n! iteratively (for comparison).

    Args:
        n: Non-negative integer

    Returns:
        int: The factorial of n
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"n must be an integer, got {type(n).__name__}")
    if n < 0:
        raise ValueError(f"n must be non-negative, got {n}")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


class RecursionTracer:
    """Helper class to visualize recursion tree."""

    def __init__(self):
        self.calls: List[str] = []
        self.depth = 0
        self.max_depth = 0

    def trace_call(self, n: int):
        """Record a function call."""
        self.depth += 1
        self.max_depth = max(self.max_depth, self.depth)
        indent = "  " * (self.depth - 1)
        self.calls.append(f"{indent}factorial({n})")

    def trace_return(self, n: int, result: int):
        """Record a return value."""
        indent = "  " * (self.depth - 1)
        self.calls.append(f"{indent}  → {result}")
        self.depth -= 1


def factorial_with_steps(n: int) -> Tuple[int, List[str]]:
    """Calculate factorial recursively and return recursion trace.

    Args:
        n: Non-negative integer

    Returns:
        Tuple of (factorial value, list of recursion steps)
    """
    # Input validation
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"n must be an integer, got {type(n).__name__}")
    if n < 0:
        raise ValueError(f"n must be non-negative, got {n}")

    tracer = RecursionTracer()

    def _factorial(x: int) -> int:
        tracer.trace_call(x)
        if x == 0 or x == 1:
            result = 1
            tracer.trace_return(x, result)
            return result
        else:
            sub_result = _factorial(x - 1)
            result = x * sub_result
            tracer.trace_return(x, result)
            return result

    result = _factorial(n)
    return result, tracer.calls


def print_factorial_demo(n: int, title: str = "FACTORIAL"):
    """Pretty print factorial calculation with recursion trace.

    Args:
        n: Number to calculate factorial for
        title: Title for the demonstration
    """
    print("\n" + "=" * 70)
    print(f"  {title}: {n}!")
    print("=" * 70)

    try:
        result, steps = factorial_with_steps(n)
        print(f"  Рекурсивний розрахунок {n}!:")
        print("  " + "-" * 60)
        for step in steps:
            print(f"  {step}")
        print("  " + "-" * 60)
        print(f"  Результат: {n}! = {result}")
        print("=" * 70)
    except Exception as e:
        print(f"  ✗ Помилка: {e}")
        print("=" * 70)


if __name__ == "__main__":
    print("\n" + "█" * 70)
    print("█  РЕКУРСИВНЕ ОБЧИСЛЕННЯ ФАКТОРІАЛУ")
    print("█" * 70)

    # Test 1: Small factorial (0)
    print("\n[Тест 1] Факторіал 0")
    print_factorial_demo(0, "0!")

    # Test 2: Small factorial (1)
    print("\n[Тест 2] Факторіал 1")
    print_factorial_demo(1, "1!")

    # Test 3: Small factorial (5)
    print("\n[Тест 3] Факторіал 5")
    print_factorial_demo(5, "5!")

    # Test 4: Medium factorial (7)
    print("\n[Тест 4] Факторіал 7")
    print_factorial_demo(7, "7!")

    # Test 5: Comparison - recursive vs iterative
    print("\n[Тест 5] Порівняння: рекурсивний vs ітеративний")
    n = 10
    result_rec = factorial_recursive(n)
    result_iter = factorial_iterative(n)
    print(f"  factorial_recursive({n}) = {result_rec}")
    print(f"  factorial_iterative({n}) = {result_iter}")
    print(f"  Результати збігаються: {result_rec == result_iter} ✓" if result_rec == result_iter else "  ✗ ПОМИЛКА")

    # Test 6: Large factorial (15)
    print("\n[Тест 6] Факторіал 15")
    result = factorial_recursive(15)
    print(f"  15! = {result}")

    # Test 7: Error handling - negative number
    print("\n[Тест 7] Обробка помилки: від'ємне число")
    try:
        factorial_recursive(-5)
    except ValueError as e:
        print(f"  ✓ Перехвачена помилка: {e}")

    # Test 8: Error handling - float
    print("\n[Тест 8] Обробка помилки: дробове число")
    try:
        factorial_recursive(5.5)
    except TypeError as e:
        print(f"  ✓ Перехвачена помилка: {e}")

    # Test 9: Error handling - string
    print("\n[Тест 9] Обробка помилки: рядок")
    try:
        factorial_recursive("п'ять")
    except TypeError as e:
        print(f"  ✓ Перехвачена помилка: {e}")

    # Test 10: Memoization test
    print("\n[Тест 10] Тест мемоізації")
    memo_dict = {}
    result1 = factorial_recursive(6, memo_dict)
    print(f"  Перший виклик factorial_recursive(6, memo): {result1}")
    print(f"  Мемоізовані значення: {memo_dict}")
    result2 = factorial_recursive(8, memo_dict)
    print(f"  Другий виклик factorial_recursive(8, memo): {result2}")
    print(f"  Мемоізовані значення: {memo_dict}")

    # Interactive mode
    print("\n" + "█" * 70)
    print("█  ІНТЕРАКТИВНИЙ РЕЖИМ")
    print("█" * 70)

    while True:
        print("\n1. Обчислити факторіал з детальною рекурсією")
        print("2. Обчислити факторіал (тільки результат)")
        print("3. Порівняти рекурсивний та ітеративний методи")
        print("4. Вихід")
        choice = input("\nВиберіть опцію (1-4): ").strip()

        if choice == "4":
            print("До побачення!")
            break

        if choice not in ["1", "2", "3"]:
            print("Невірна опція.")
            continue

        print("\nВведіть невід'ємне ціле число:")
        user_input = input(">>> ").strip()

        try:
            n_val = int(user_input)

            if choice == "1":
                print_factorial_demo(n_val, f"ФАКТОРІАЛ {n_val}")

            elif choice == "2":
                result = factorial_recursive(n_val)
                print(f"\n{n_val}! = {result}")

            elif choice == "3":
                result_rec = factorial_recursive(n_val)
                result_iter = factorial_iterative(n_val)
                print(f"\n  Рекурсивний метод:  {n_val}! = {result_rec}")
                print(f"  Ітеративний метод:  {n_val}! = {result_iter}")
                print(f"  Результати рівні: {result_rec == result_iter} ✓")

        except ValueError as e:
            print(f"✗ Помилка: {e}")
        except TypeError as e:
            print(f"✗ Помилка: {e}")
        except Exception as e:
            print(f"✗ Невідома помилка: {e}")

    # Summary info
    print("\n" + "=" * 70)
    print("  ІНФОРМАЦІЯ ПРО ФАКТОРІАЛ")
    print("=" * 70)
    print("""
  Факторіал числа n (позначається n!) - це добуток всіх додатних
  цілих чисел від 1 до n включно.

  Визначення:
    0! = 1 (за визначенням)
    n! = n × (n-1)! для n > 0

  Приклади:
    0! = 1
    1! = 1
    2! = 2 × 1 = 2
    3! = 3 × 2 × 1 = 6
    4! = 4 × 3 × 2 × 1 = 24
    5! = 5 × 4 × 3 × 2 × 1 = 120

  Рекурсивна реалізація:
    - Базові випадки: 0! = 1, 1! = 1
    - Рекурсивний випадок: n! = n × (n-1)!
    - Часова складність: O(n)
    - Просторова складність: O(n) (через стек викликів)

  Ітеративна реалізація:
    - Використовує цикл від 2 до n
    - Часова складність: O(n)
    - Просторова складність: O(1)
    - Зазвичай швидша за рекурсивну

  Мемоізація:
    - Збереження результатів попередніх обчислень
    - Зменшує кількість повторних обчислень
    - Корисна при множинних викликах
    """)
    print("=" * 70)
