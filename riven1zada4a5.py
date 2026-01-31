"""Compute geometric series 1 + x + x^2 + ... + x^n and display as a formula.

Provides:
- geometric_sum(x, n): validates inputs and returns numeric sum
- series_str(x, n): returns string like "1+2+2^2+...+2^n = sum"
- CLI for interactive use
"""
from typing import Union

Number = Union[int, float]


def _format_base(x: Number) -> str:
    """Format base `x` for human-friendly output."""
    if isinstance(x, int):
        return str(x)
    # for float, show without trailing .0 when possible
    if isinstance(x, float) and x.is_integer():
        return str(int(x))
    return str(x)


def geometric_sum(x: Number, n: int) -> Number:
    """Return sum 1 + x + x^2 + ... + x^n.

    Validates that `n` is a non-negative integer and `x` is numeric.
    Uses closed-form formula when x != 1.
    """
    # validate n
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    # validate x
    if not isinstance(x, (int, float)) or isinstance(x, bool):
        raise TypeError("x must be a number (int or float)")

    if n == 0:
        return 1
    if x == 1:
        return n + 1
    # use pow to support negative and float bases
    return (x ** (n + 1) - 1) / (x - 1)


def series_str(x: Number, n: int, show_sum: bool = True) -> str:
    """Return a string representation of the series and optionally the sum.

    Example: series_str(2, 3) -> '1+2+2^2+2^3 = 15'
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")

    base = _format_base(x)
    terms = []
    for i in range(n + 1):
        if i == 0:
            terms.append("1")
        elif i == 1:
            terms.append(base)
        else:
            terms.append(f"{base}^{i}")
    expr = "+".join(terms)
    if show_sum:
        val = geometric_sum(x, n)
        # if value is close to integer, format as int
        if isinstance(val, float) and abs(val - round(val)) < 1e-12:
            val = int(round(val))
        return f"{expr} = {val}"
    return expr


if __name__ == "__main__":
    print("\nГЕОМЕТРИЧНА СУММА: 1 + x + x^2 + ... + x^n")
    try:
        raw_x = input("Введіть значення x (наприклад 2 або 1.5): ").strip()
        raw_n = input("Введіть ціле невід'ємне n (наприклад 3): ").strip()

        # parse x
        try:
            x_val = int(raw_x) if raw_x.lstrip('-').isdigit() else float(raw_x)
        except Exception:
            raise ValueError("Невірний формат для x")

        # parse n
        if not raw_n.lstrip('-').isdigit():
            raise ValueError("n повинен бути цілим числом")
        n_val = int(raw_n)

        # compute and print
        result_str = series_str(x_val, n_val, show_sum=True)
        print("\nРезультат:")
        print(result_str)
    except Exception as e:
        print(f"Помилка: {e}")
