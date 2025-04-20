# program to create logic for palindrome of string and integer

def Spalindrome(s):
    #s = s.lower() # this fun use to convert lowercase.
    return s == s[::-1]

print(Spalindrome("madam"))
print(Spalindrome("Tat"))
print(Spalindrome("python"))

def Npalindrome(n):
    n = str(n)
    return n == n[::-1]

print(Npalindrome(121))
print(Npalindrome(123))
