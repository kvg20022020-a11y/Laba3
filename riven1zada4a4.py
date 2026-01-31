"""Cyclic shift of list elements.

This module provides functions to perform cyclic (circular) rotation
of list elements with step-by-step output after each transformation.
"""

from typing import List, Tuple
import copy


def rotate_list_right(lst: List[int], step: int = 1) -> List[int]:
    """Perform a single right cyclic shift on the list.
    
    Shifts elements to the right. Elements that exit on the right
    reappear on the left side (cyclic/circular).
    
    Args:
        lst: List of integers to rotate
        step: Number of positions to shift right (default: 1)
              Can be negative (shifts left instead)
        
    Returns:
        List[int]: New rotated list
        
    Examples:
        >>> rotate_list_right([1, 2, 3, 4, 5], 1)
        [5, 1, 2, 3, 4]
        >>> rotate_list_right([1, 2, 3, 4, 5], 2)
        [4, 5, 1, 2, 3]
    """
    if not lst or len(lst) == 0:
        return lst
    
    # Normalize step to list length
    step = step % len(lst)
    
    if step == 0:
        return lst.copy()
    
    # Use list slicing for rotation
    return lst[-step:] + lst[:-step]


def rotate_list_left(lst: List[int], step: int = 1) -> List[int]:
    """Perform a single left cyclic shift on the list.
    
    Shifts elements to the left. Elements that exit on the left
    reappear on the right side (cyclic/circular).
    
    Args:
        lst: List of integers to rotate
        step: Number of positions to shift left (default: 1)
              Can be negative (shifts right instead)
        
    Returns:
        List[int]: New rotated list
        
    Examples:
        >>> rotate_list_left([1, 2, 3, 4, 5], 1)
        [2, 3, 4, 5, 1]
        >>> rotate_list_left([1, 2, 3, 4, 5], 2)
        [3, 4, 5, 1, 2]
    """
    if not lst or len(lst) == 0:
        return lst
    
    # Normalize step to list length
    step = step % len(lst)
    
    if step == 0:
        return lst.copy()
    
    # Use list slicing for rotation
    return lst[step:] + lst[:step]


def cyclic_shift_repeated(lst: List[int], step: int, 
                         times: int, direction: str = "right",
                         show_steps: bool = True) -> Tuple[List[int], List[List[int]]]:
    """Perform cyclic shift repeatedly with step-by-step output.
    
    Args:
        lst: List of integers to rotate
        step: Number of positions to shift per operation
        times: Number of times to perform the shift
        direction: "right" or "left" direction of rotation
        show_steps: If True, prints each step
        
    Returns:
        Tuple containing:
            - Final rotated list
            - List of all intermediate states
    """
    if not lst:
        return lst, [lst.copy()]
    
    if times < 0:
        raise ValueError("times must be non-negative")
    
    if direction not in ["right", "left"]:
        raise ValueError("direction must be 'right' or 'left'")
    
    current = lst.copy()
    history = [current.copy()]
    
    rotate_func = rotate_list_right if direction == "right" else rotate_list_left
    
    for i in range(times):
        current = rotate_func(current, step)
        history.append(current.copy())
        
        if show_steps:
            print(f"  Крок {i+1}: {current}")
    
    return current, history


def cyclic_shift_inplace(lst: List[int], step: int, 
                        times: int, direction: str = "right") -> None:
    """Perform cyclic shift repeatedly, modifying list in-place.
    
    Args:
        lst: List to modify in-place
        step: Number of positions to shift per operation
        times: Number of times to perform the shift
        direction: "right" or "left" direction of rotation
    """
    if not lst or len(lst) == 0:
        return
    
    rotate_func = rotate_list_right if direction == "right" else rotate_list_left
    
    for _ in range(times):
        rotated = rotate_func(lst, step)
        lst.clear()
        lst.extend(rotated)


def print_shift_demo(lst: List[int], step: int, times: int, 
                    direction: str = "right", title: str = "CYCLIC SHIFT"):
    """Pretty print cyclic shift demonstration.
    
    Args:
        lst: List of integers
        step: Shift step
        times: Number of iterations
        direction: "right" or "left"
        title: Title for the demonstration
    """
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)
    print(f"  Вихідний список: {lst}")
    print(f"  Напрямок: {'вправо →' if direction == 'right' else '← вліво'}")
    print(f"  Крок зміщення: {step}")
    print(f"  Кількість повторень: {times}")
    print("=" * 70)
    
    result, history = cyclic_shift_repeated(lst, step, times, direction, show_steps=True)
    
    print("=" * 70)
    print(f"  Результат: {result}")
    print("=" * 70)


if __name__ == "__main__":
    print("\n" + "█" * 70)
    print("█  ЦИКЛІЧНЕ ЗМІЩЕННЯ ЕЛЕМЕНТІВ СПИСКУ")
    print("█" * 70)
    
    # Test 1: Right shift by 1
    print("\n[Тест 1] Зміщення вправо на 1 позицію, 3 рази")
    print_shift_demo([1, 2, 3, 4, 5], step=1, times=3, direction="right",
                    title="Зміщення вправо →")
    
    # Test 2: Left shift by 1
    print("\n[Тест 2] Зміщення вліво на 1 позицію, 3 рази")
    print_shift_demo([1, 2, 3, 4, 5], step=1, times=3, direction="left",
                    title="Зміщення вліво ←")
    
    # Test 3: Right shift by 2
    print("\n[Тест 3] Зміщення вправо на 2 позиції, 2 рази")
    print_shift_demo([10, 20, 30, 40, 50], step=2, times=2, direction="right",
                    title="Зміщення вправо на 2")
    
    # Test 4: Large step
    print("\n[Тест 4] Зміщення вправо на 7 позицій (більше за розмір), 2 рази")
    print_shift_demo([1, 2, 3, 4, 5], step=7, times=2, direction="right",
                    title="Великий крок (7 > len)")
    
    # Test 5: Complete rotation cycle
    print("\n[Тест 5] Повна ротація (5 кроків для списку з 5 елементів)")
    print_shift_demo([1, 2, 3, 4, 5], step=1, times=5, direction="right",
                    title="Повна ротація вправо")
    
    # Test 6: Multiple elements shift
    print("\n[Тест 6] Більший список, зміщення на 3, 4 рази")
    print_shift_demo(list(range(1, 11)), step=3, times=4, direction="left",
                    title="Список 1-10, зміщення вліво на 3")
    
    # Test 7: Single element list
    print("\n[Тест 7] Список з одного елемента")
    print_shift_demo([42], step=1, times=3, direction="right",
                    title="Один елемент")
    
    # Test 8: Two elements
    print("\n[Тест 8] Список з двох елементів")
    print_shift_demo([100, 200], step=1, times=4, direction="right",
                    title="Два елементи")
    
    # Test 9: Letters representation
    print("\n[Тест 9] Наочна демонстрація з буквами")
    print_shift_demo(['A', 'B', 'C', 'D', 'E'], step=1, times=3, direction="right",
                    title="Букви, зміщення вправо")
    
    # Test 10: Negative numbers
    print("\n[Тест 10] Від'ємні числа")
    print_shift_demo([-5, -3, 0, 2, 4], step=2, times=3, direction="left",
                    title="Від'ємні числа, зміщення вліво на 2")
    
    # Interactive mode
    print("\n" + "█" * 70)
    print("█  ІНТЕРАКТИВНИЙ РЕЖИМ")
    print("█" * 70)
    
    while True:
        print("\n1. Зміщення вправо")
        print("2. Зміщення вліво")
        print("3. Вихід")
        choice = input("\nВиберіть опцію (1-3): ").strip()
        
        if choice == "3":
            print("До побачення!")
            break
        
        if choice not in ["1", "2"]:
            print("Невірна опція.")
            continue
        
        direction = "right" if choice == "1" else "left"
        arrow = "→" if direction == "right" else "←"
        
        # Get list from user
        print("\nВведіть список цілих чисел (розділені пробілом):")
        list_input = input(">>> ").strip()
        
        try:
            numbers = []
            for num in list_input.split():
                numbers.append(int(num))
            
            if not numbers:
                print("Помилка: список не може бути порожнім")
                continue
            
            # Get shift step
            step_input = input("\nВведіть крок зміщення: ").strip()
            step = int(step_input)
            
            if step < 0:
                print("Помилка: крок повинен бути невід'ємним")
                continue
            
            # Get number of times
            times_input = input("Введіть кількість повторень: ").strip()
            times = int(times_input)
            
            if times < 0:
                print("Помилка: кількість повторень повинна бути невід'ємною")
                continue
            
            if times == 0:
                print("Список залишається без змін")
                continue
            
            # Perform shift
            print_shift_demo(numbers, step=step, times=times, direction=direction,
                           title=f"Зміщення {arrow} на {step}, {times} разів")
        
        except ValueError as e:
            print(f"✗ Помилка введення: невірний формат числа")
        except Exception as e:
            print(f"✗ Помилка: {e}")
    
    # Additional info
    print("\n" + "=" * 70)
    print("  ІНФОРМАЦІЯ ПРО ЦИКЛІЧНЕ ЗМІЩЕННЯ")
    print("=" * 70)
    print("""
  Циклічне (кільцеве) зміщення - це операція, при якій елементи списку
  зміщуються на вказану кількість позицій, а елементи, які виходять за
  межі списку з одного кінця, з'являються з іншого кінця.
  
  Приклади:
  • Список [1, 2, 3, 4, 5] зміщений вправо на 1: [5, 1, 2, 3, 4]
    (5 вийшла справа, з'явилась зліва)
  
  • Список [1, 2, 3, 4, 5] зміщений вліво на 1: [2, 3, 4, 5, 1]
    (1 вийшла зліва, з'явилась справа)
  
  Формула для нормалізації кроку: step = step % len(list)
  Це гарантує, що навіть великі кроки дадуть правильний результат.
  
  Часова складність: O(n) для одного зміщення
  Просторова складність: O(n) для збереження копії списку
    """)
    print("=" * 70)
