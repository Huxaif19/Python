import string
def pallindrome(s):
    s = s.replace(' ', '')
    return s == s[::-1] 
print(pallindrome('racecar'))
def panagram(str1, alphabet = string.ascii_lowercase):
    alphaset = set(alphabet)
    str1 = str1.replace(" ", '')
    st1= str1.lower()
    str1 = set(str1)
    return str1 == alphaset
print(panagram('qwertyuioplkjhgfdsazxcvbnmmm'))