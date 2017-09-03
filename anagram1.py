def anagramSolution4(s1,s2):
    c1 = [0]*26
    c2 = [0]*26
    if len(s1) == len(s2):

        for i in range(len(s1)):
            pos = ord(s1[i])-ord('a')
            c1[pos] += 1

        for i in range(len(s2)):
            pos = ord(s2[i])-ord('a')
            c2[pos] += 1

        j = 0

        while j<26:
            if c1[j]==c2[j]:
                j = j + 1
            else:
                return False

        return True
    else:
        return False


print(anagramSolution4('apple','pleap'))


