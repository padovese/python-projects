class Song(object):
    def __init__(self, lyrics):
        print self
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you", "I don't want to get sued","So I'll stop right there"])
aaa = Song("aaabbbcc")


happy_bday.sing_me_a_song()
aaa.sing_me_a_song()