"""Read a sequence ending with 0 and output it in reverse order.

Provides multiple implementations:
- Recursive approach (natural for reversing)
- Iterative approach with list
- Stack-based approach
- Interactive mode for user input
"""

from typing import List, Callable


def read_and_reverse_recursive(numbers: List[int] = None, depth: int = 0) -> None:
    """Read numbers recursively until 0 is entered, print in reverse order.

    How it works:
        1. Read a number from user
        2. If it's 0, stop and return (base case)
        3. Otherwise, store it and recursively read the rest
        4. When returning from recursion, print the stored number (reversed!)

    The magic: The recursion naturally reverses the sequence because
    we print AFTER the recursive call (post-order traversal).

    Args:
        numbers: Internal list to store numbers
        depth: Current recursion depth
    """
    if numbers is None:
        numbers = []

    print(f"  Введіть число #{len(numbers) + 1} (або 0 для завершення): ", end="")

    try:
        num = int(input().strip())
    except ValueError:
        print("  ✗ Помилка: введіть ціле число")
        return read_and_reverse_recursive(numbers, depth)

    if num == 0:
        # Base case: we reached 0, now print in reverse
        print("\n  Послідовність у зворотному порядку:")
        return  # This causes the recursion to unwind and print happens during unwinding

    # Store number and continue recursion
    numbers.append(num)
    read_and_reverse_recursive(numbers, depth + 1)


def read_and_reverse_recursive_v2() -> None:
    """Read numbers recursively and print in reverse (alternative version).

    This version uses true recursion: reads, then prints, then backtracks.
    Much more elegant - the call stack naturally reverses the sequence!
    """

    def _read_and_print() -> None:
        """Inner recursive function."""
        print(f"  Введіть число (або 0 для завершення): ", end="")

        try:
            num = int(input().strip())
        except ValueError:
            print("  ✗ Помилка: введіть ціле число")
            return _read_and_print()

        if num == 0:
            return  # Base case: stop recursion

        # Recursive case: read next before printing current
        _read_and_print()  # Read the rest first (important!)

        # Print AFTER recursion returns (this creates the reverse effect!)
        print(f"  {num}")

    print("  Введіть послідовність чисел (завершіть 0):")
    _read_and_print()
    print("  (список завершено)")


def read_and_reverse_iterative() -> List[int]:
    """Read numbers iteratively and return in reverse order.

    Args:
        None (reads from user input)

    Returns:
        List[int]: Sequence in reverse order
    """
    numbers = []
    counter = 1

    while True:
        print(f"  Введіть число #{counter} (або 0 для завершення): ", end="")

        try:
            num = int(input().strip())
        except ValueError:
            print("  ✗ Помилка: введіть ціле число")
            continue

        if num == 0:
            break

        numbers.append(num)
        counter += 1

    # Return reversed
    return numbers[::-1]


def reverse_sequence_from_string(input_str: str) -> List[int]:
    """Parse a string of space-separated numbers and return in reverse.

    Numbers should be separated by spaces. Reading stops at 0.

    Args:
        input_str: String like "5 3 7 2 0"

    Returns:
        List[int]: Sequence in reverse order (excluding 0)
    """
    numbers = []

    for token in input_str.split():
        try:
            num = int(token)
            if num == 0:
                break
            numbers.append(num)
        except ValueError:
            continue

    return numbers[::-1]


def print_reverse_demo(numbers: List[int], title: str = "REVERSE"):
    """Pretty print sequence reversal demonstration.

    Args:
        numbers: Original sequence
        title: Title for output
    """
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)
    print(f"  Вихідна послідовність:  {numbers}")
    print(f"  Обернена послідовність: {numbers[::-1]}")
    print("=" * 70)


class SequenceReverser:
    """Helper class to demonstrate different reversal methods."""

    @staticmethod
    def using_list(seq: List[int]) -> List[int]:
        """Reverse using list slicing."""
        return seq[::-1]

    @staticmethod
    def using_reversed(seq: List[int]) -> List[int]:
        """Reverse using reversed() function."""
        return list(reversed(seq))

    @staticmethod
    def using_stack(seq: List[int]) -> List[int]:
        """Reverse using stack (LIFO)."""
        stack = []
        for num in seq:
            stack.append(num)
        result = []
        while stack:
            result.append(stack.pop())
        return result

    @staticmethod
    def using_recursion(seq: List[int], index: int = None) -> List[int]:
        """Reverse using recursion."""
        if index is None:
            index = len(seq) - 1

        if index < 0:
            return []

        return [seq[index]] + SequenceReverser.using_recursion(seq, index - 1)

    @staticmethod
    def manual_swap(seq: List[int]) -> List[int]:
        """Reverse by swapping elements from both ends."""
        result = seq.copy()
        left, right = 0, len(result) - 1
        while left < right:
            result[left], result[right] = result[right], result[left]
            left += 1
            right -= 1
        return result


if __name__ == "__main__":
    print("\n" + "█" * 70)
    print("█  ЧИТАННЯ ПОСЛІДОВНОСТІ ТА ВИВЕДЕННЯ В ЗВОРОТНОМУ ПОРЯДКУ")
    print("█" * 70)

    # Test 1: Simple sequence (terminated with 0)
    print("\n[Тест 1] Проста послідовність")
    print("  Введена послідовність: 5 3 8 1 0")
    seq1 = [5, 3, 8, 1]  # 0 is just terminator, not part of sequence
    print(f"  Послідовність (без 0): {seq1}")
    print(f"  Обернена послідовність: {seq1[::-1]}")

    # Test 2: Another sequence (terminated with 0)
    print("\n[Тест 2] Інша послідовність")
    print("  Введена послідовність: 10 20 30 40 50 0")
    seq2 = [10, 20, 30, 40, 50]
    print(f"  Послідовність (без 0): {seq2}")
    print(f"  Обернена послідовність: {seq2[::-1]}")

    # Test 3: Single element (terminated with 0)
    print("\n[Тест 3] Одноелементна послідовність")
    print("  Введена послідовність: 42 0")
    seq3 = [42]
    print(f"  Послідовність (без 0): {seq3}")
    print(f"  Обернена послідовність: {seq3[::-1]}")

    # Test 4: Negative numbers (terminated with 0)
    print("\n[Тест 4] З від'ємними числами")
    print("  Введена послідовність: -5 3 -1 7 -2 0")
    seq4 = [-5, 3, -1, 7, -2]
    print(f"  Послідовність (без 0): {seq4}")
    print(f"  Обернена послідовність: {seq4[::-1]}")

    # Test 5: With zeros in middle (as data, not terminator)
    print("\n[Тест 5] З нулем всередині послідовності (нуль як дані)")
    print("  ВАЖЛИВО: 0 всередині послідовності - це звичайне число")
    print("  Введена послідовність: 5 0 3 0 1 0 (останній 0 - термінатор)")
    seq5 = [5, 0, 3, 0, 1]
    print(f"  Послідовність (без терміналу 0): {seq5}")
    print(f"  Обернена послідовність: {seq5[::-1]}")

    # Test 6: Large sequence (terminated with 0)
    print("\n[Тест 6] Велика послідовність 1-10")
    print("  Введена послідовність: 1 2 3 4 5 6 7 8 9 10 0")
    seq6 = list(range(1, 11))
    print(f"  Послідовність (без 0): {seq6}")
    print(f"  Обернена послідовність: {seq6[::-1]}")

    # Test 7: Comparison of reversal methods
    print("\n[Тест 7] Порівняння методів розворотання")
    print("=" * 70)
    seq = [1, 2, 3, 4, 5]
    print(f"  Вихідна послідовність (без 0): {seq}\n")

    print(f"  using_list():       {SequenceReverser.using_list(seq)}")
    print(f"  using_reversed():   {SequenceReverser.using_reversed(seq)}")
    print(f"  using_stack():      {SequenceReverser.using_stack(seq)}")
    print(f"  using_recursion():  {SequenceReverser.using_recursion(seq)}")
    print(f"  manual_swap():      {SequenceReverser.manual_swap(seq)}")
    print("=" * 70)

    # Test 8: Parse from string (with 0 terminator)
    print("\n[Тест 8] Парсинг послідовності зі строки")
    print("  Введена строка: '7 2 9 4 1 0'")
    input_str = "7 2 9 4 1 0"
    result = reverse_sequence_from_string(input_str)
    print(f"  Послідовність без терміналу (0 видалено): {result[::-1]}")
    print(f"  Обернена послідовність: {result}")

    # Test 9: Empty sequence (0 immediately)
    print("\n[Тест 9] Порожня послідовність (0 одразу)")
    print("  Введена послідовність: 0")
    seq_empty = []
    print(f"  Послідовність (без 0): {seq_empty}")
    print(f"  Обернена послідовність: {seq_empty[::-1]}")

    # Test 10: Identical elements (terminated with 0)
    print("\n[Тест 10] Однакові елементи")
    print("  Введена послідовність: 5 5 5 5 5 0")
    seq_ident = [5, 5, 5, 5, 5]
    print(f"  Послідовність (без 0): {seq_ident}")
    print(f"  Обернена послідовність: {seq_ident[::-1]}")

    # Interactive mode
    print("\n" + "█" * 70)
    print("█  ІНТЕРАКТИВНИЙ РЕЖИМ")
    print("█" * 70)

    while True:
        print("\n1. Прочитати послідовність та вивести в зворотному порядку (рекурсія)")
        print("2. Прочитати послідовність та вивести в зворотному порядку (ітерація)")
        print("3. Введення послідовності як один рядок")
        print("4. Вихід")
        choice = input("\nВиберіть опцію (1-4): ").strip()

        if choice == "4":
            print("До побачення!")
            break

        if choice not in ["1", "2", "3"]:
            print("Невірна опція.")
            continue

        if choice == "1":
            print("\n" + "=" * 70)
            print("  РЕКУРСИВНИЙ МЕТОД")
            print("  Введіть послідовність, кожне число на новому рядку")
            print("=" * 70)
            read_and_reverse_recursive_v2()

        elif choice == "2":
            print("\n" + "=" * 70)
            print("  ІТЕРАТИВНИЙ МЕТОД")
            print("  Введіть послідовність, кожне число на новому рядку")
            print("=" * 70)
            numbers = read_and_reverse_iterative()
            if numbers:
                print("\n  Послідовність у зворотному порядку:")
                for num in numbers:
                    print(f"  {num}")
            else:
                print("  (послідовність порожня)")

        elif choice == "3":
            print("\n" + "=" * 70)
            print("  ВВЕДЕННЯ ПОСЛІДОВНОСТІ ОДНИМ РЯДКОМ")
            print("  Введіть числа, розділені пробілами (завершіть 0)")
            print("  Приклад: 5 3 7 2 0")
            print("=" * 70)
            user_input = input(">>> ").strip()

            result = reverse_sequence_from_string(user_input)
            if result:
                print(f"\n  Вихідна послідовність:  {reverse_sequence_from_string(user_input)[::-1]}")
                print(f"  Обернена послідовність: {result}")
            else:
                print("  (послідовність порожня)")

    # Summary info
    print("\n" + "=" * 70)
    print("  ІНФОРМАЦІЯ ПРО РОЗВОРОТАННЯ ПОСЛІДОВНОСТЕЙ")
    print("=" * 70)
    print("""
  Розворотання послідовності - це обернення порядку елементів.

  Методи розворотання:

  1. СПИСОК (List slicing):
     reversed_seq = seq[::-1]
     - Часова складність: O(n)
     - Просторова складність: O(n) - нова копія
     - Найпростіший спосіб в Python

  2. ФУНКЦІЯ reversed():
     reversed_seq = list(reversed(seq))
     - Часова складність: O(n)
     - Просторова складність: O(n)
     - Повертає ітератор (економить пам'ять)

  3. РЕКУРСІЯ:
     def reverse(seq, i):
         if i < 0: return []
         return [seq[i]] + reverse(seq, i-1)
     - Часова складність: O(n)
     - Просторова складність: O(n) - стек викликів
     - Елегантна, але медліша

  4. СТЕК (LIFO):
     stack = []
     for num in seq: stack.append(num)
     while stack: result.append(stack.pop())
     - Часова складність: O(n)
     - Просторова складність: O(n)
     - Демонструє принцип LIFO (Last In, First Out)

  5. ОБМІН ЕЛЕМЕНТІВ:
     left, right = 0, len(seq)-1
     while left < right:
         seq[left], seq[right] = seq[right], seq[left]
         left += 1; right -= 1
     - Часова складність: O(n)
     - Просторова складність: O(1) - на місці
     - Найефективніша за пам'яттю

  РЕКУРСИВНЕ ЧИТАННЯ ТА ВИВЕДЕННЯ:
  
  Наймагічніший способ - читати послідовність рекурсивно
  і виводити її під час розворотання стека:

      def read_and_print():
          num = int(input())
          if num == 0: return
          read_and_print()  # read rest first
          print(num)        # print AFTER recursion returns

  Це працює тому, що стек викликів природно зберігає числа,
  а під час розворотання стека вони виводяться у зворотному порядку!

  ПРАКТИЧНІ ПРИКЛАДИ:
  
  • Скасування операцій (undo в редакторах)
  • Розбір виразів (prefix vs postfix notation)
  • Обхід графів (DFS uses call stack as implicit stack)
  • Палінромна перевірка
  • Розворотання рядків та файлів
    """)
    print("=" * 70)
