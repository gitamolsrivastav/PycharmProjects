def bruteSearch(text, pattern):
    i = 0
    n = len(text)
    m = len(pattern)
    c =  0
    diff = n-m
    while i <= diff:
        j =0
        while j < m and pattern[j] == text[i+j]:
            j += 1
        if  j == m:
            c += 1
        i += 1

    return c


print(bruteSearch("ABCDEFGHEFGTEFG", "EFG"))


