# # #################################program31#################################
#
# def rev(x):
#     r = []
#     xlen = len(x)
#     sIndex = xlen -1
#     while sIndex >= 0:
#         r.append(x[sIndex])
#         sIndex = sIndex -1
#     revString = "".join(r)
#     return revString
#
# print(rev("I am who I am "))
#
#
# #################################program2#################################
# def pali(s):
#
#     slen = len(s)
#     high = slen -1
#     low = 0
#     while high != low:
#         if s[high] == s[low]:
#             high -= 1
#             low +=1
#         else:
#             return False
#     return True
#
#
# print(pali("mooodaoom"))
#
# #################################program3#################################

def char_frequency(x):
    x = list(x)
    d ={}
    for i in x:
        if i not in d:
            d[i]= 1
        else:
            d[i] += 1
        #d[i] = d.get(i,0) + 1
    
        print(d.items())
    print( "".join(["%s%s" % (k, v) for k, v in d.items()]))




char_frequency([1,1,2,3,4,4,6,7,8,9])


