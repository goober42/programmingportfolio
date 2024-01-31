import random

listroot = ["ambi", "bene", "circum", "dict", "form", "fract", "ject", "mal", "multi", "pater", "spect", "voc", "rupt", "mater", "mort","mit","scrib","sect", "contra", "cent"]
listprefix = ["anti", "de", "dis", "fore", "inter", "mid", "mis", "non", "over", "pre", "semi", "sub", "super", "trans", "un", "under", "up", "ex", "in", "re"]
listsuffix = ["able", "ial", "ed", "en", "er", "est", "ful", "ic", "ing", "ion", "less","tion","ation", "ity", "ive", "ize", "less", "ly", "ment", "ness", "ous",]

listrootdef = ["both", "good", "around", "word", "shape", "part", "cut", "bad", "many", "father", " look", "sound", "break", "mother", "death", "to send","write","cut", "against", "one hundred"]
listprefixdef = [" being against ", " opposite of ", " not ", " before or in front of ", " between ", " in the middle of ", " wrongly ", " not ", " too much ", " before ", " partly ", " less ", " obove or beyond ", " accross ", " opposite of ", " too little ", " being above ", " out of ", " in ", " again "]
listsuffixdef = ["can be", "having characteristics of", "past tense", "made of", "more", "the most", "full of", "having characteristics of", "in the process of", "the act of", "without", "the act of", "the act of", "state of", "being in the state of", "to conform or resemble", "without", "like" , "state of being" , "state of", "full of"]

count = int(input("how many words do you want?"))
while count > 0:

  x = random.randint(0,len(listroot)-1)
  y = random.randint(0,len(listprefix)-1)
  z = random.randint(0,len(listsuffix)-1)

  word = listroot[x] + listprefix[y] + listsuffix[z]

  print(word)

  definition = listsuffixdef[z] + listprefixdef[y] +   listrootdef[x]

  print("definition:" + definition)
  count -=1

