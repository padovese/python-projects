from sys import argv
script, filename = argv

txt = open(filename).read()

print "the content of the file is: "
print txt