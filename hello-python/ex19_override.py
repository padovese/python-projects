class Parent(object):
    def speak(self):
        print "Hello, i am the dad"

class Son(Parent):
    pass

Parent().speak()
Son().speak()




class Parent2(object):
    def speak(self):
        print "Hello, i am the dad"

class Son2(Parent2):
    def speak(self):
        print "Hello, i am the son"

Parent2().speak()
Son2().speak()