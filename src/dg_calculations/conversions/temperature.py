"""Fahrenheit Subtract 32, then multiply by 5/9ths Celsius
Celsius Multiply by 9/5ths, then add 32 Fahrenheit"""


def c_to_f(temp: float) -> float:
    return (temp * (9 / 5)) + 32


def f_to_c(temp: float) -> float:
    return (temp - 32) * (5 / 9)
