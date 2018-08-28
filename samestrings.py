def editDistance(str1, str2, m ,n):
    """"""
    if m == 0:
        return n
    if n == 0:
        return m
    if str1[m-1] == str[m-2]:
        return editDistance(str1, str2, m-1, m-2)
    else:
        return 1 + min()
str1 = "sunday"
str2 = "saturday"
print editDistance(str1, str2, len(str1), len(str2))