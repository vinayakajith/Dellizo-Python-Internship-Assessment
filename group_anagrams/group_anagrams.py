def group_anagrams(words):
    groups = {}
    for word in words:
        # Sort letters in word to make a key
        key = ''.join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    # Return the groups as a list of lists
    return list(groups.values())

# Example use
words = ["bat", "tab", "cat", "act", "tac", "tap", "pat"]
print(group_anagrams(words))
