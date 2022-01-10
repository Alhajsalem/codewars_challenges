def sortme(words):
    sorted_list = sorted(words, key=lambda s: s.lower())
    return sorted_list


sortme(["C", "d", "a", "B"])
#, ["a", "B", "C", "d"])
#, ["fine", "Hello", "I'm", "there"]