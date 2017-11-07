# Define your compute function here.
# run python -m unittest test.hamming_test to ensure the
# unit tests pass and your code meets all of the conditions.
#


def compute(s1, s2):

    if len(s1) != len(s2):
        raise ValueError("Length of s1 != length of s2, invalid data...")

    return sum(c1 != c2 for c1, c2 in zip(s1, s2))
