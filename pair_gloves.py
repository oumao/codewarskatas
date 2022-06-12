from collections import Counter
def find_pair(gloves):
    return len([(key, key) for key, val in Counter(gloves).items() for _ in range(val//2)])


print(find_pair(["gray","black","purple","purple","gray","black"]))
print(find_pair(["White","Yellow","Fuchsia","Red","Silver","Gray","Olive","Purple", "Navy", "Lime", "Maroon","Aqua","Lime","Teal","Green","Blue","Navy","Black"]))