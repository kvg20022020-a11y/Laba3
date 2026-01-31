"""Integer exponentiation (supports positive and negative integer exponents).

Provides:
- pow_int(base, exp): iterative fast exponentiation (binary exponentiation)
- pow_int_recursive(base, exp): recursive fast exponentiation
- Input validation and handling of zero base with negative exponent
- CLI and tests
"""
from typing import Union

Number = Union[int, float]


def _validate_input(base: Number, exp: int) -> None:
    if isinstance(exp, bool) or not isinstance(exp, int):
        raise TypeError("Exponent must be an integer")
    if not isinstance(base, (int, float)) or isinstance(base, bool):
        raise TypeError("Base must be a number (int or float)")


def pow_int(base: Number, exp: int) -> Number:
    """Compute base ** exp where exp is integer (positive, zero, or negative).

    Uses iterative binary exponentiation. For negative exponent returns float (1/base**|exp|).

    Raises:
        TypeError: if types are invalid
        ZeroDivisionError: if base == 0 and exp < 0
    """
    _validate_input(base, exp)

    if exp == 0:
        return 1

    if base == 0:
        if exp < 0:
            raise ZeroDivisionError("0 cannot be raised to a negative power")
        return 0

    negative = exp < 0
    e = -exp if negative else exp

    result = 1
    b = float(base) if negative else base

    # Binary exponentiation
    while e > 0:
        if e & 1:
            result = result * b
        b = b * b
        e >>= 1

    if negative:
        return 1.0 / result
    return result


def pow_int_recursive(base: Number, exp: int) -> Number:
    """Recursive binary exponentiation supporting negative exponents."""
    _validate_input(base, exp)

    if exp == 0:
        return 1
    if base == 0:
        if exp < 0:
            raise ZeroDivisionError("0 cannot be raised to a negative power")
        return 0

    if exp < 0:
        return 1.0 / pow_int_recursive(base, -exp)

    # exp > 0
    if exp % 2 == 0:
        half = pow_int_recursive(base, exp // 2)
        return half * half
    else:
        return base * pow_int_recursive(base, exp - 1)


if __name__ == "__main__":
    # Simple tests
    tests = [
        (2, 10),
        (2, -3),
        (5, 0),
        (0, 5),
        (3, 1),
        (2.5, 3),
        (2, -1),
    ]

    print("Quick tests for pow_int and pow_int_recursive:")
    for base, exp in tests:
        try:
            it = pow_int(base, exp)
            rec = pow_int_recursive(base, exp)
            print(f"  {base}^{exp} -> iterative: {it}, recursive: {rec}")
        except Exception as e:
            print(f"  {base}^{exp} -> Error: {e}")

    # Interactive
    print("\nInteractive mode: compute base^exp where exp is integer")
    try:
        raw_base = input("Enter base (e.g. 2 or 2.5): ").strip()
        raw_exp = input("Enter integer exponent (e.g. -3, 0, 4): ").strip()

        base_val = int(raw_base) if raw_base.lstrip('-').isdigit() else float(raw_base)
        if not raw_exp.lstrip('-').isdigit():
            raise ValueError("Exponent must be integer")
        exp_val = int(raw_exp)

        print(f"Iterative: {base_val}^{exp_val} = {pow_int(base_val, exp_val)}")
        print(f"Recursive: {base_val}^{exp_val} = {pow_int_recursive(base_val, exp_val)}")

    except Exception as e:
        print(f"Error: {e}")
