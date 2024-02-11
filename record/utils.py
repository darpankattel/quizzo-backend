import math


def transform_to_level(x):
    """
    Transforms a decimal number x (xp) to a value between 0 and 10 (level).
    The transformation starts with fast growth and transitions to slow growth.
    """
    if x <= 20:
        # Fast growth: linear mapping from [0, 20] to [0, 1]
        return x / 20.0
    elif x <= 100:
        # Slow growth: logarithmic mapping from (20, 100] to (1, 2]
        return 1 + math.log(x / 20.0, 5)  # Base 5 logarithm
    elif x <= 300:
        # Slower growth: linear mapping from (100, 300] to (2, 3]
        return 2 + (x - 100) / 200.0
    else:
        # Final stretch: linear mapping from (300, 2500] to (3, 10]
        return 3 + (x - 300) / 2200.0
