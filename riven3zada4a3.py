"""
Task: Create a text file with 9 lines where line n contains n letters 'a'.

Example output:
a
aa
aaa
aaaa
...
aaaaaaaaa
"""

def create_letter_file(filename: str, rows: int = 9, char: str = 'a') -> None:
    """
    Create a text file where each line n contains n repetitions of char.
    
    Args:
        filename: Path to output file
        rows: Number of lines (default 9)
        char: Character to repeat (default 'a')
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for i in range(1, rows + 1):
                f.write(char * i + '\n')
        print(f"[OK] File '{filename}' created successfully with {rows} lines")
    except IOError as e:
        print(f"[ERROR] Error creating file: {e}")


def print_preview(rows: int = 9, char: str = 'a') -> None:
    """Print preview of what will be written."""
    print(f"\nPreview ({rows} lines):")
    print("-" * 20)
    for i in range(1, rows + 1):
        print(char * i)
    print("-" * 20)


if __name__ == "__main__":
    import sys
    
    # Get filename from argument or use default
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "output.txt"
    
    # Show preview
    print_preview()
    
    # Create file
    create_letter_file(filename)
    
    # Show file content
    print(f"\nFile contents:")
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            print(content)
    except IOError as e:
        print(f"Error reading file: {e}")
