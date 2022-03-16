str1 = str(input('Enter First String : ')).strip().replace(' ', '').lower()
str2 = str(input('Enter Second String : ')).strip().replace(' ', '').lower()


def Ch_anagram(s1, s2):
    if len(s1) == len(s2):
        length = len(s1)
        same_chars = 0
        for x in range(0, length):
            if s1.count(s1[x]) == s2.count(s1[x]):
                same_chars += 1
        if length == same_chars:
            print("We can form < {} > using the chars of < {} > , So given two strings are anagrams".format(s1, s2))
        else:
            print(
                "We can't form < {} > using the chars of < {} > , So given two strings are Not anagrams".format(s1, s2))
    else:
        print("Length of < {} > is not equal to < {} > so it's not an anagram".format(s1, s2))


Ch_anagram(str1, str2)
