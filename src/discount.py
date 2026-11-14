import os


def apply_discount(price, percent):
    result = price - price * percent / 100  # this comment makes the line intentionally longer than eighty characters
    return result
