"""Recursive implementation of Fibonacci sequence with multiple optimization strategies.

Provides:
- fibonacci_recursive(n): Basic recursive implementation
- fibonacci_memoized(n): Recursive with memoization (optimized)
- fibonacci_iterative(n): Iterative implementation (fastest)
- fibonacci_generator(n): Generator for Fibonacci sequence
- Recursion tree visualization and performance comparisons
"""

from typing import Dict, List, Tuple
import time


def fibonacci_recursive(n: int, call_count: Dict[int, int] = None) -> int:
    """Calculate n-th Fibonacci number using basic recursion.

    Definition:
        F(0) = 0
        F(1) = 1
        F(n) = F(n-1) + F(n-2) for n > 1

    WARNING: Very inefficient for large n due to exponential time complexity.
    Recommended only for n <= 35.

    Args:
        n: Non-negative integer (index in Fibonacci sequence)
        call_count: Internal dict to count recursive calls

    Returns:
        int: The n-th Fibonacci number

    Raises:
        TypeError: If n is not an integer
        ValueError: If n is negative
    """
    # Input validation
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"n must be an integer, got {type(n).__name__}")
    if n < 0:
        raise ValueError(f"n must be non-negative, got {n}")

    # Initialize call counter
    if call_count is None:
        call_count = {}

    # Count calls for analysis
    call_count[n] = call_count.get(n, 0) + 1

    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Recursive case: F(n) = F(n-1) + F(n-2)
    return fibonacci_recursive(n - 1, call_count) + fibonacci_recursive(n - 2, call_count)


def fibonacci_memoized(n: int, memo: Dict[int, int] = None) -> int:
    """Calculate n-th Fibonacci number using recursion with memoization.

    Memoization stores previously computed values to avoid redundant calculations.
    Much more efficient than basic recursion: O(n) instead of O(2^n).

    Args:
        n: Non-negative integer
        memo: Memoization cache (internal use)

    Returns:
        int: The n-th Fibonacci number
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"n must be an integer, got {type(n).__name__}")
    if n < 0:
        raise ValueError(f"n must be non-negative, got {n}")

    # Initialize memoization cache
    if memo is None:
        memo = {}

    # Check if already computed
    if n in memo:
        return memo[n]

    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Recursive case with memoization
    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]


def fibonacci_iterative(n: int) -> int:
    """Calculate n-th Fibonacci number using iteration.

    Most efficient approach: O(n) time, O(1) space.

    Args:
        n: Non-negative integer

    Returns:
        int: The n-th Fibonacci number
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"n must be an integer, got {type(n).__name__}")
    if n < 0:
        raise ValueError(f"n must be non-negative, got {n}")

    if n == 0:
        return 0
    if n == 1:
        return 1

    prev2, prev1 = 0, 1
    for _ in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1


def fibonacci_generator(max_n: int):
    """Generate Fibonacci sequence up to n-th number.

    Args:
        max_n: Maximum index to generate

    Yields:
        int: Fibonacci numbers from F(0) to F(max_n)
    """
    if not isinstance(max_n, int) or isinstance(max_n, bool):
        raise TypeError("max_n must be an integer")
    if max_n < 0:
        raise ValueError("max_n must be non-negative")

    a, b = 0, 1
    for i in range(max_n + 1):
        if i == 0:
            yield 0
        elif i == 1:
            yield 1
        else:
            a, b = b, a + b
            yield b


class FibonacciTracer:
    """Helper class to visualize Fibonacci recursion tree."""

    def __init__(self, max_depth: int = 10):
        self.calls: List[str] = []
        self.depth = 0
        self.max_depth = max_depth
        self.call_count = 0

    def trace_call(self, n: int):
        """Record a function call."""
        if self.depth >= self.max_depth:
            return

        self.call_count += 1
        indent = "  " * self.depth
        self.calls.append(f"{indent}fib({n})")
        self.depth += 1

    def trace_return(self, n: int, result: int):
        """Record a return value."""
        self.depth -= 1
        if self.depth < self.max_depth:
            indent = "  " * self.depth
            self.calls.append(f"{indent}  → {result}")


def fibonacci_with_steps(n: int, max_depth: int = 6) -> Tuple[int, List[str]]:
    """Calculate Fibonacci with recursion trace (limited depth for readability).

    Args:
        n: Index of Fibonacci number
        max_depth: Maximum recursion depth to show

    Returns:
        Tuple of (fibonacci value, list of recursion steps)
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"n must be an integer, got {type(n).__name__}")
    if n < 0:
        raise ValueError(f"n must be non-negative, got {n}")

    tracer = FibonacciTracer(max_depth=max_depth)

    def _fib(x: int) -> int:
        tracer.trace_call(x)
        if x == 0:
            result = 0
        elif x == 1:
            result = 1
        else:
            result = _fib(x - 1) + _fib(x - 2)
        tracer.trace_return(x, result)
        return result

    result = _fib(n)
    return result, tracer.calls


def print_fibonacci_demo(n: int, title: str = "FIBONACCI"):
    """Pretty print Fibonacci calculation with recursion trace.

    Args:
        n: Index of Fibonacci number
        title: Title for the demonstration
    """
    print("\n" + "=" * 70)
    print(f"  {title}: F({n})")
    print("=" * 70)

    try:
        result, steps = fibonacci_with_steps(n, max_depth=6)
        print(f"  Рекурсивний розрахунок F({n}):")
        print("  " + "-" * 60)
        for step in steps[:100]:  # Limit output
            print(f"  {step}")
        if len(steps) > 100:
            print(f"  ... (скорочено, всього {len(steps)} рядків)")
        print("  " + "-" * 60)
        print(f"  Результат: F({n}) = {result}")
        print("=" * 70)
    except Exception as e:
        print(f"  ✗ Помилка: {e}")
        print("=" * 70)


def print_sequence(n: int):
    """Print Fibonacci sequence from F(0) to F(n).

    Args:
        n: Maximum index to display
    """
    print("\n" + "=" * 70)
    print(f"  ПОСЛІДОВНІСТЬ ФІБОНАЧЧІ: F(0) до F({n})")
    print("=" * 70)

    sequence = list(fibonacci_generator(n))
    print("  Індекс │ Число Фібоначчі")
    print("  " + "-" * 40)
    for i, fib_num in enumerate(sequence):
        print(f"  F({i:2d})  │ {fib_num:>20}")
    print("=" * 70)


if __name__ == "__main__":
    print("\n" + "█" * 70)
    print("█  ПОСЛІДОВНІСТЬ ФІБОНАЧЧІ: РЕКУРСИВНА РЕАЛІЗАЦІЯ")
    print("█" * 70)

    # Test 1: Small Fibonacci numbers
    print("\n[Тест 1] Послідовність F(0) до F(10)")
    print_sequence(10)

    # Test 2: Recursion trace for F(6)
    print("\n[Тест 2] Дерево рекурсії для F(6)")
    print_fibonacci_demo(6, "F(6)")

    # Test 3: Recursion trace for F(7)
    print("\n[Тест 3] Дерево рекурсії для F(7)")
    print_fibonacci_demo(7, "F(7)")

    # Test 4: Comparison of three methods
    print("\n[Тест 4] Порівняння трьох методів для F(10)")
    print("=" * 70)
    n = 10
    result_rec = fibonacci_recursive(n)
    result_memo = fibonacci_memoized(n)
    result_iter = fibonacci_iterative(n)
    print(f"  fibonacci_recursive({n}) = {result_rec}")
    print(f"  fibonacci_memoized({n})  = {result_memo}")
    print(f"  fibonacci_iterative({n}) = {result_iter}")
    if result_rec == result_memo == result_iter:
        print(f"  ✓ Все результати рівні")
    print("=" * 70)

    # Test 5: Performance comparison
    print("\n[Тест 5] Порівняння продуктивності")
    print("=" * 70)

    test_cases = [15, 20, 25, 30]

    for n in test_cases:
        print(f"\n  n = {n}:")

        # Basic recursion (skip if too large)
        if n <= 30:
            start = time.time()
            result_rec = fibonacci_recursive(n)
            time_rec = time.time() - start
            print(f"    Рекурсія:      {time_rec:.6f} сек → {result_rec}")
        else:
            print(f"    Рекурсія:      (пропущена, надто повільна)")

        # Memoized
        start = time.time()
        result_memo = fibonacci_memoized(n)
        time_memo = time.time() - start
        print(f"    Мемоізація:    {time_memo:.6f} сек → {result_memo}")

        # Iterative
        start = time.time()
        result_iter = fibonacci_iterative(n)
        time_iter = time.time() - start
        print(f"    Ітерація:      {time_iter:.6f} сек → {result_iter}")

    print("=" * 70)

    # Test 6: Base cases
    print("\n[Тест 6] Базові випадки")
    print(f"  F(0) = {fibonacci_iterative(0)}")
    print(f"  F(1) = {fibonacci_iterative(1)}")
    print(f"  F(2) = {fibonacci_iterative(2)}")

    # Test 7: Error handling
    print("\n[Тест 7] Обробка помилок")
    test_errors = [
        (-5, "від'ємне число"),
        (5.5, "дробове число"),
        ("п'ять", "рядок"),
    ]

    for val, desc in test_errors:
        try:
            fibonacci_iterative(val)
        except (TypeError, ValueError) as e:
            print(f"  ✓ {desc}: {type(e).__name__}")

    # Test 8: Large Fibonacci
    print("\n[Тест 8] Велике число Фібоначчі")
    n = 50
    result = fibonacci_memoized(n)
    print(f"  F({n}) = {result}")

    # Test 9: Call count analysis
    print("\n[Тест 9] Аналіз кількості викликів функції")
    print("=" * 70)
    n = 10
    call_count = {}
    result = fibonacci_recursive(n, call_count)
    total_calls = sum(call_count.values())
    print(f"  F({n}) обчислено базовою рекурсією")
    print(f"  Всього викликів функції: {total_calls}")
    print(f"  Результат: {result}")
    print("=" * 70)

    # Test 10: Generator test
    print("\n[Тест 10] Використання генератора")
    print("  Перші 12 чисел Фібоначчі (через генератор):")
    fibs = list(fibonacci_generator(11))
    print(f"  {fibs}")

    # Interactive mode
    print("\n" + "█" * 70)
    print("█  ІНТЕРАКТИВНИЙ РЕЖИМ")
    print("█" * 70)

    while True:
        print("\n1. Показати послідовність Фібоначчі до n")
        print("2. Обчислити F(n) з детальною рекурсією")
        print("3. Порівняти методи обчислення")
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
                print_sequence(min(n_val, 20))  # Limit to 20 for readability

            elif choice == "2":
                if n_val <= 15:
                    print_fibonacci_demo(n_val, f"F({n_val})")
                else:
                    result = fibonacci_memoized(n_val)
                    print(f"\nF({n_val}) = {result}")
                    print("(Детальна рекурсія не показується для n > 15)")

            elif choice == "3":
                result_memo = fibonacci_memoized(n_val)
                result_iter = fibonacci_iterative(n_val)
                print(f"\n  fibonacci_memoized({n_val})  = {result_memo}")
                print(f"  fibonacci_iterative({n_val}) = {result_iter}")
                print(f"  Результати рівні: {result_memo == result_iter} ✓")

        except ValueError as e:
            print(f"✗ Помилка: {e}")
        except TypeError as e:
            print(f"✗ Помилка: {e}")
        except Exception as e:
            print(f"✗ Невідома помилка: {e}")

    # Summary info
    print("\n" + "=" * 70)
    print("  ІНФОРМАЦІЯ ПРО ПОСЛІДОВНІСТЬ ФІБОНАЧЧІ")
    print("=" * 70)
    print("""
  Послідовність Фібоначчі - це послідовність чисел, в якій кожне число
  дорівнює сумі двох попередніх чисел.

  Визначення:
    F(0) = 0
    F(1) = 1
    F(n) = F(n-1) + F(n-2) для n > 1

  Послідовність: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

  Рекурсивна реалізація:
    - Простий в розумінні код
    - Часова складність: O(2^n) - експоненціальна!
    - Просторова складність: O(n) - стек викликів
    - НЕВЖИННА для n > 35 (занадто повільна)

  Мемоізована реалізація:
    - Зберігає результати у словник
    - Часова складність: O(n) - лінійна
    - Просторова складність: O(n) - кеш + стек
    - РЕКОМЕНДУЄТЬСЯ для рекурсивного підходу

  Ітеративна реалізація:
    - Використовує цикл
    - Часова складність: O(n) - лінійна
    - Просторова складність: O(1) - константна
    - НАЙЕФЕКТИВНІША за мінімум пам'яті

  Практичне застосування:
    - Природа: спіралі, листя, кістки
    - Математика: Золотий переріз
    - Комп'ютерна графіка: алгоритми поділу простору
    - Аналіз алгоритмів: складність операцій
    """)
    print("=" * 70)
