from collections import Counter
def find_pair(gloves):
    res = len([(key, key) for key, val in Counter(gloves).items() for _ in range(val//2)])