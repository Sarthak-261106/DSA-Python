# a=input('enter string:')
# b=input("enter pattern:")

# def computeLPS(str, lps):
#     n=len(str)

#     i=1
#     temp=0
#     while i<n:
#         if str[i]==str[temp]:
#             temp+=1
#             lps[i]=temp
#             i+=1
#         else:
#             if temp!=0:
#                 temp=lps[temp-1]
#             else:
#                 lps[i]=0
#                 i+=1

#         return         


# def kmp(neddle, haystack):
#     n=len(haystack)
#     m=len(neddle)
#     lps=[0]*m

#     computeLPS(neddle, lps)

#     i=0
#     j=0
#     while i<n:
#         if haystack[i]==neddle[j]:
#             i+=1
#             j+=1

#         if j==m:
#             return i-j
#         elif i<n and neddle[i]!=haystack[j]:
#             if j!=0:
#                 j=lps[j-1]
#             else:
#                 i+=1

#         return -1          

# kmp(a,b)

haystack=input('enter string:')
needle=input("enter pattern:")

def computeLPS(str, lps):
        n=len(str)

        i=1
        temp=0
        while i<n:
            if str[i]==str[temp]:
                temp+=1
                lps[i]=temp
                i+=1
            else:
                if temp!=0:
                    temp=lps[temp-1]
                else:
                    lps[i]=0
                    i+=1

            
        
def kmpalgo(haystack,needle):
    n=len(haystack)
    m=len(needle)
    lps=[0]*m

    computeLPS(needle, lps)

    i=0
    j=0
    while i<n:
        if haystack[i]==needle[j]:
            i+=1
            j+=1

        if j==m:
            return i-j
        elif i<n and haystack[i]!=needle[j]:
            if j!=0:
                j=lps[j-1]
            else:
                i+=1

    return -1

print(kmpalgo(haystack,needle))        