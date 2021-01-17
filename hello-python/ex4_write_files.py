from sys import argv
script, filename = argv

txt = open(filename, "w")

content =  raw_input("write the content: ")
txt.write(content)

print "the result is:"

txt = open(filename)
print txt.read()

