print "Oh,"
print "hello there"
print "mr. python!"
#commented lines

print 1+1
print 2*2
print 1 >= 0


car = "Audi"
spaces = 4
potency = 1.8
print car
print spaces
print potency

print "The car is an %s" % car
print "The car is %s, has %i spaces and the potency is %d" % (car, spaces, potency)

print round(potency)

print "." * 10


print "%r %r %r" % ("one", "two", "three") #r is for debug, print exactly the type
print "%s %s %s" % ("one", "two", "three")

print "branking \n line"

print """Paragraph
like
Kotlin"""

print "the car is " + car
print "the car is ", car

print "Tell me your age:"
age = raw_input()
print "You have live %s days" % (int(age)*365)

anotgerAge = raw_input("Tell me your age: ")
print anotgerAge
