import os


def apply_discount(price, percent):
    # short comment
    result = price - price * percent / 100
    return result
