def anagram_checker(s1,s2):
   s2_list = list(s2)
   pos1 = 0
   ok = True
   while pos1 < len(s1) and ok:
      pos2 = 0
      found = False
      while pos2 < len(s2_list) and not found:
         if s1[pos1] == s2_list[pos2]:
            found = True
         else:
            pos2 = pos2 + 1
      if found:
         s2_list[pos2] = None   #checking off the second list if match found
      else:
         ok = False
      pos1 = pos1 + 1
   return ok
print(anagram_checker('abcde','dcba'))