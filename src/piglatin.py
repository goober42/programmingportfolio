sentence = input().lower()
words = sentence.split()
latin_words = []

vowels = ['a','e','i','o','u']

for word in words:
    has_vowel = False

    for i in range(len(word)):
  
        if word[0] in vowels:
            latin_words.append(word + "yay")
            break
        else:

            if word[i] in vowels:
                latin_words.append(word[i:] + word[:i] + "ay")
                has_vowel = True
                break

            if(has_vowel == False and i == len(word)-1):
                latin_words.append(word + "ay")
                break

pig_latin_sentence = ' '.join(latin_words)
print(pig_latin_sentence)