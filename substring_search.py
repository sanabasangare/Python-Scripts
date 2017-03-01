'''I started by preparing edge cases in the event when the inputs are the same, 
or if an entry is “None”, or simply empty, then a TypeError is raised. 
To find possible substrings in a string "s", I stored the characters of "t" 
separately. Then, created a new (empty) dict to store the substrings of string 
"s" that are the same length as "t". And lastly, if the substrings in the dicts 
are a match, the function returns True.'''

'''The average time complexity for this solution is O(n^2) because the inner 
loop will iterate j times for each iterations of the outer loop i.'''


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

print substring_ngram(" ", "abc")       	# False

print substring_ngram("abc@#$", "@#$")  	# True

print substring_ngram("silent", "listen")  	# True

print substring_ngram("testing", "set")  	# True

print substring_ngram("warning", None)  	# String Required!

print substring_ngram("warning", "wng")  	# False
