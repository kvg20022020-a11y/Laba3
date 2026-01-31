"""Count lines, words and characters in a text file.

Usage:
    - Import `count_file_stats` and call with a path
    - Run as script and enter a filename (or pass as first arg)

Definition:
    - lines: number of newline-terminated lines in file
    - words: tokens separated by any whitespace (split())
    - chars: number of characters (includes newlines)
"""
from typing import Dict
import sys
import os


def count_file_stats(path: str, encoding: str = "utf-8") -> Dict[str, int]:
    """Return dictionary with counts: {'lines': int, 'words': int, 'chars': int}.

    Raises FileNotFoundError or UnicodeDecodeError if file unreadable.
    """
    if not isinstance(path, str):
        raise TypeError("path must be a string")

    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    lines = 0
    words = 0
    chars = 0

    with open(path, "r", encoding=encoding) as f:
        for line in f:
            lines += 1
            chars += len(line)
            # split on any whitespace
            words += len(line.split())

    return {"lines": lines, "words": words, "chars": chars}


def _print_stats(path: str, stats: Dict[str, int]) -> None:
    print(f"File: {path}")
    print(f"Lines: {stats['lines']}")
    print(f"Words: {stats['words']}")
    print(f"Characters: {stats['chars']}")


if __name__ == "__main__":
    # Accept path as first CLI arg or ask user
    path = None
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = input("Enter path to text file: ").strip()

    # Sanitize common issues: extra quotes or surrounding whitespace
    if path is not None:
        path = path.strip().strip('"').strip("'")

    if not path:
        print("No path provided.")
    else:
        try:
            stats = count_file_stats(path)
            _print_stats(path, stats)
        except FileNotFoundError as e:
            print(f"Error: {e}")
            # Diagnostic information to help locate the file
            import os
            print("Diagnostics:")
            print("  repr(path):", repr(path))
            print("  os.path.exists(path):", os.path.exists(path))
            parent = os.path.dirname(path)
            print("  Parent dir:", parent)
            try:
                listing = os.listdir(parent)
                print("  Parent directory listing (first 50 entries):")
                for entry in listing[:50]:
                    print("   ", entry)
            except Exception as le:
                print("  Could not list parent directory:", le)
        except UnicodeDecodeError:
            print("Error: cannot decode file with utf-8 encoding. Try another encoding.")
        except Exception as e:
            print(f"Unexpected error: {e}")
