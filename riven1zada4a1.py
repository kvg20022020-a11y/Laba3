"""Utilities for counting unique characters in a string.

Provides a dictionary-based implementation and a NumPy-based variant.
Scipy is not required for this task; NumPy's `unique` covers it.
"""

from typing import Dict


def count_chars_dict(s: str) -> Dict[str, int]:
	"""Return a dictionary mapping each character in `s` to its count.

	Args:
		s: input string

	Returns:
		dict: {character: count}
	"""
	counts: Dict[str, int] = {}
	for ch in s:
		counts[ch] = counts.get(ch, 0) + 1
	return counts


def unique_char_count(s: str) -> int:
	"""Return the number of unique characters in `s` using the dict counter."""
	return len(count_chars_dict(s))


def count_chars_numpy(s: str) -> Dict[str, int]:
	"""Return a dict of character counts using NumPy's `unique`.

	Requires `numpy` to be installed. This is provided as an alternative
	approach; `scipy` is not necessary for this task.
	"""
	try:
		import numpy as np
	except ImportError as e:
		raise ImportError("numpy is required for count_chars_numpy") from e

	if len(s) == 0:
		return {}

	arr = np.array(list(s), dtype='<U1')
	unique, counts = np.unique(arr, return_counts=True)
	# Convert NumPy types to native Python
	return {u: int(c) for u, c in zip(unique.tolist(), counts.tolist())}


if __name__ == "__main__":
    # Get user input
    user_input = input("Введіть текст для аналізу: ")
    
    if not user_input:
        print("Помилка: текст не може бути порожнім.")
    else:
        print(f"\nАналіз тексту: '{user_input}'")
        print("=" * 50)

        # Dictionary-based counting
        d = count_chars_dict(user_input)
        print(f"Словник символів: {d}")
        print(f"Кількість унікальних символів: {unique_char_count(user_input)}")

        # NumPy variant (if NumPy available)
        print("=" * 50)
        try:
            dn = count_chars_numpy(user_input)
            print(f"NumPy варіант: {dn}")
        except ImportError:
            print("NumPy не встановлений; пропускаємо NumPy варіант.")
