def group_anagrams(strs):
    groups = []
    letters = []

    for word in strs:
        counts = {}
        for letter in word:
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1

        found = False
        for i in range(len(groups)):
            if counts == letters[i]:
                groups[i].append(word)
                found = True
                break

        if not found:
            groups.append([word])
            letters.append(counts)

    return groups
