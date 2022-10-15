# 3.2 - Matching Pairs 

def matching_pairs(s, t):
    # CHECK FOR VALID INPUT
    if len(s) != len(t):
        raise ValueError(f"Strings have different lengths.")
    if len(s) < 2:
        raise ValueError(f"Length of strings {len(s)} precludes a swap being possible.")

    # CHECK FOR MATCHING STRINGS
    if s == t:
        if contains_repeat_char(s):
            # any repeated characters can be swapped with impunity
            return len(s)
        else:
            # must impose a swap, which reduces matches
            return len(s) - 2

    # TRAVERSE THE STRINGS
    # Count the matching pairs while saving data about the pairs for a potential swap later
    misses = set()  # non-matching pairs
    pairs = set()  # the swap pool
    base = 0 # pre-swap count of matching pairs

    for si, ti in zip(s, t):
        pairs.add((si, ti))
        if si == ti:
            base += 1
            pairs.add((si, True))  # matched pair swap candidate
        else:
            misses.add((si, ti))
            pairs.add((si, False))   # unmatched pair swap candidate

    # CHECK FOR SPECIFIC MISSES THAT CAN BE SWAPPED
    # CHECK THEM IN SERIAL ORDER BECAUSE EACH SWAP TYPES IMPACT THE MATCH COUNT DIFFERENTLY
    
    # Check for a swap that creates two new matches: eg. pre-swap s='ab', t='ba'; after swap s='ba'
    for m in misses:
        if (m[1], m[0]) in pairs: return base + 2
    # Check for a swap that creates one new match: eg. pre-swap s='at', t='xa'; after swap s='ta'
    for m in misses:
        if (m[1], False) in pairs: return base + 1
    # Check for a swap that breaks an existing match while creating a new one: eg. pre-swap s='ab', t='aa'; after swap s='ba'
    for m in misses:
        if (m[1], True) in pairs: return base

    # CHECK FOR REPEATED CHARACTERS IN 's', which can be swapped with impunity
    if contains_repeat_char(s):
        return base

    # IMPOSE A SWAP
    # 2 indices that both contain misses can be swapped with impunity
    if len(misses) >= 2:
        return base

    # swapping an index that has a miss with an index that has a match removes a match
    if len(misses) == 1 and base >= 1:
        return base - 1

    # else, swap indexes of two matching pairs, which removes both matches
    return base - 2

def contains_repeat_char(str):
    used = set()
    for c in str:
        if c in used:
            return True
        else:
            used.add(c)
    return False

s_1, t_1 = "abcde", "adcbe"
expected_1 = 5
print(matching_pairs(s_1, t_1))