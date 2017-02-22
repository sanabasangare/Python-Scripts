def Longest_Palindromic_Substring(a):
    if a == None or not isinstance(a, str):
        return TypeError("String Required!")

    longest_pal = 1
    start = 0
    length = len(a)

    for i in xrange(1, length):
        # assuming i in every character as the starting point of this search
        low = i - 1
        high = i + 1
        while low >= 0 and high < length and a[low] == a[high]:
            if high - low + 1 > longest_pal:
                start = low
                longest_pal = high - low + 1
            low -= 1
            high += 1

    return a[start:start + longest_pal]


print Longest_Palindromic_Substring("Mississippi")  # ississi

print Longest_Palindromic_Substring("abcacbada")    # abcacba

print Longest_Palindromic_Substring("acbcacdc")     # acbca

print Longest_Palindromic_Substring("")             # (empty space)

print Longest_Palindromic_Substring("qqaabcba")     # abcba

print Longest_Palindromic_Substring("abcd")         # a

print Longest_Palindromic_Substring(None)           # String Required!

print Longest_Palindromic_Substring(1117779) 		# String Required!
