message = "foydieruberxoyv oy vobhxyd rjg wunnbg, wbgevg xyfbuag rjg loia “VOBURXOY” xy poui fohgi bgrrgi, ebvo lixrg e weiediewj gkwbexyxyd rjg wiov eya foyv om uvxyd e wevvloia qeyedgi."

file = open('data.txt', 'r')
data = file.readlines()

# Combine all lines into a single string
words = " ".join(data)

# Cut the new line syntax
words = words.replace("\n", "")

# Separate into each word
words_split = words.split(" ")

match_all = []

# Condition checking for the first encoded word "foydieruberxoyv"
for word in words_split:
    if word[1] == word[12] and word[2] == word[13] and word[6] == word[10] and word[5] == word[9]:
        match_all.append(word)

encoder = "foydieruberxoyv"

decoder = {'h': 'v', 'j':'h', 'g':'e', 'a':'d', 'p':'y', 'l':'w', 'k':'x', 'w':'p', 'n':'z', 'm':'f', 'q':'m'}


i = 0

while i < len(encoder):
    if decoder.get(encoder[i]) is None:
        decoder[encoder[i]] = match_all[0][i].lower()
    i += 1

result = ""

for i in message:
    for key in decoder:
        if i.lower() not in decoder.keys() and i != " ":
            # result += "[{}]".format(i) # Show undecrypeted
            result += i
            break
        elif i == " ":
            result += i
            break
        elif i.lower() == key:
            result += decoder[i.lower()]
            break

# a = sorted(decoder.keys())
# b = sorted(decoder.values())
# print(a)
# print(b)
print(message)
print(result)
