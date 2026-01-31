"""
Find lines in a text file that end with a specified character and invert them.

Functions:
 - find_and_invert_lines(path, char, encoding='utf-8', ignore_trailing_whitespace=True)

CLI: Interactive mode - prompts for file path and target character.
"""

from typing import List, Tuple
import sys
import os


def find_and_invert_lines(path: str, char: str, encoding: str = 'utf-8', ignore_trailing_whitespace: bool = True) -> List[Tuple[str, str]]:
    """Find lines ending with `char` and return both original and inverted versions.

    Args:
        path: Path to the text file.
        char: Character to check for at end of each line.
        encoding: File encoding to use when opening the file.
        ignore_trailing_whitespace: If True, trailing spaces and tabs are ignored when checking the last character.

    Returns:
        List of tuples (original_line, inverted_line).
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    if char is None or len(char) == 0:
        raise ValueError("`char` must be a non-empty string")

    results = []
    with open(path, 'r', encoding=encoding, errors='replace') as f:
        for raw in f:
            # Remove newline characters
            s = raw.rstrip('\r\n')
            check_str = s.rstrip() if ignore_trailing_whitespace else s
            
            if check_str and check_str.endswith(char):
                inverted = s[::-1]
                results.append((s, inverted))
    
    return results


def _clean_path(p: str) -> str:
    """Clean file path from quotes and extra whitespace."""
    return p.strip().strip('"').strip("'")


if __name__ == "__main__":
    print("=" * 60)
    print("Програма для інвертування рядків з файлу")
    print("=" * 60)
    
    # Get file path
    path = _clean_path(input("\nВведіть шлях до текстового файлу: "))
    if not path:
        print("Шлях не вказано. Вихід.")
        sys.exit(1)

    if not os.path.exists(path):
        print(f"Файл не знайдено: {repr(path)}")
        parent = os.path.dirname(path) or "."
        try:
            print("Вміст батьківської директорії (перші 10 файлів):")
            files = os.listdir(parent)[:10]
            for f in files:
                print(f"  - {f}")
        except Exception:
            print("Не вдалося прочитати батьківську директорію.")
        sys.exit(1)

    # Get target character
    char = input("Введіть символ, яким повинні закінчуватись рядки: ")
    if len(char) == 0:
        print("Символ не вказано. Використано пробіл.")
        char = " "

    # Process file
    try:
        results = find_and_invert_lines(path, char)
        
        print(f"\n{'=' * 60}")
        print(f"Знайдено рядків, що закінчуються на '{char}': {len(results)}")
        print(f"{'=' * 60}\n")
        
        if len(results) == 0:
            print("Жодного рядка не знайдено.")
        else:
            for i, (original, inverted) in enumerate(results, 1):
                print(f"Рядок {i}:")
                print(f"  Оригінал:   {original}")
                print(f"  Інвертовано: {inverted}")
                print()
        
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")
        sys.exit(1)
