def substring_ngram(s, t):
    # If there is no string input
    if s == None or t == None:
        return TypeError('String Required!')

    # If the string and substring are the same, return True
    if s == t:
        return True

    # changing both strings to all lowercase.
    s = s.lower()
    t = t.lower()

    # creating a dict for the string
    s_dict = {}

    # iterating and adding the characters in t to the empty dict
    for i in range(len(t)):
        s_dict[t[i]] = t.count(t[i])

    # creates a new dict "t_dict" for the substrings in s of length t
    for i in range(len(s) - len(t) + 1):
        s_sub_dict = s[i:i + len(t)]
        t_dict = {}

        # stores possible substrings of s to the dict
        for j in range(len(t)):
            t_dict[s_sub_dict[j]] = s_sub_dict.count(s_sub_dict[j])

        # If the dicts match, return True
        if t_dict == s_dict:
            return True
    return False
