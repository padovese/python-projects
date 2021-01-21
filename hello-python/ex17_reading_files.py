from urllib import urlopen

url = "http://learncodethehardway.org/words.txt"

for word in urlopen(url).readlines():
    print word.capitalize()