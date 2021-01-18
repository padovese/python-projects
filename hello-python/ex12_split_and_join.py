phrase = "The world is an illuson."

splitted = phrase.split(' ')

i = 0

while len(splitted) != 10:
    splitted2 = phrase.split(' ')
    splitted.append(splitted2[i])
    i += 1

print splitted

newPhrase = " ".join(splitted)

print newPhrase

print "#".join(splitted[3:5])