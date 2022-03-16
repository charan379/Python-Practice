# Counting Vowels and consonants in a string

String = 'a e i o ui , hjk l'

vowel_count = 0
consonent_count = 0
for x in String.lower():
    if x.isalpha():
        if x in ['a','e','i','o','u']:
            vowel_count += 1
        else:
            consonent_count += 1

print(vowel_count, consonent_count)


