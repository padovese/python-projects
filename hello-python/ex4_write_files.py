from sys import argv
from os.path import exists

script, filename = argv

txt = open(filename, "w")

print "Does the file exist? %r" % exists(filename)
content =  raw_input("write the content: ")
txt.write(content)
txt.close()

print "the result is:"

txt = open(filename)
print txt.read()
print "The input file is %d bytes long" % len(txt.read())
txt.close()
