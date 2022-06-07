from collections import Counter
def find_it(seq):
    return [key for key, value in Counter(seq).items() if value%2 == 1][0]