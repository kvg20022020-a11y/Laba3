"""
Count lines in a text file that end with a given character.

Functions:
 - count_lines_ending_with(path, char, encoding='utf-8', ignore_trailing_whitespace=True)

CLI: python riven3zada4a4.py filename char [--no-strip]
"""

from typing import Tuple, List
import sys
import os


def count_lines_ending_with(path: str, char: str, encoding: str = 'utf-8', ignore_trailing_whitespace: bool = True) -> Tuple[int, List[str]]:
	"""Return the number of lines in `path` whose last non-newline character equals `char`.

	Args:
		path: Path to the text file.
		char: Character to check for at end of each line (string of length >=1).
		encoding: File encoding to use when opening the file.
		ignore_trailing_whitespace: If True, trailing spaces and tabs are ignored when checking the last character.

	Returns:
		Tuple of (count, list of matching lines).
	"""
	if not os.path.exists(path):
		raise FileNotFoundError(f"File not found: {path}")
	if char is None or len(char) == 0:
		raise ValueError("`char` must be a non-empty string")

	matching_lines = []
	with open(path, 'r', encoding=encoding, errors='replace') as f:
		for raw in f:
			# remove newline characters
			s = raw.rstrip('\r\n')
			if ignore_trailing_whitespace:
				s = s.rstrip()
			if s and s.endswith(char):
				matching_lines.append(s)
	return len(matching_lines), matching_lines


def _usage_and_exit():
	print("Usage: python riven3zada4a4.py <filename> <char> [--no-strip]")
	sys.exit(1)


if __name__ == "__main__":
    import os

    def _clean_path(p: str) -> str:
        return p.strip().strip('"').strip("'")

    path = _clean_path(input("Введіть шлях до тестового файлу: ").strip())
    if not path:
        print("Шлях не вказано. Вихід.")
        raise SystemExit(1)

    if not os.path.exists(path):
        print(f"Файл не знайдено: {repr(path)}")
        parent = os.path.dirname(path) or "."
        try:
            print("Вміст батьківської директорії (перші 50):", os.listdir(parent)[:50])
        except Exception:
            print("Не вдалося прочитати батьківську директорію.")
        raise SystemExit(1)

    char = input("Введіть символ, яким повинні закінчуватись рядки (введіть пробіл для пробілу): ")
    if len(char) == 0:
        print("Символ не вказано. Використано пробіл.")
        char = " "

    count, lines = count_lines_ending_with(path, char)
    print(f"\nКількість рядків, що закінчуються на '{char}': {count}")
    if count > 0:
        print(f"\nРядки, що закінчуються на '{char}':")
        print("-" * 50)
        for i, line in enumerate(lines, 1):
            print(f"{i}. {line}")
        print("-" * 50)

