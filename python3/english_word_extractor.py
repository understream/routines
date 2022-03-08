import sys

class StateMachine:
    NORMAL = 1
    IN_WORD = 2
    def __init__(self):
        self.state = StateMachine.NORMAL
        self.tmp = ""
        self.ret = []

    def feed(self, c):
        if self.state == StateMachine.NORMAL:
            if ('a' <= c and c <= 'z') or ('A' <= c and c <= 'Z'): 
                self.state = StateMachine.IN_WORD
                self.tmp = c
            else:
                self.state = StateMachine.NORMAL
        elif self.state == StateMachine.IN_WORD:
            if ('a' <= c and c <= 'z') or ('A' <= c and c <= 'Z'): 
                self.state == StateMachine.IN_WORD
                self.tmp += c
            else:
                self.ret.append( self.tmp )
                self.tmp = ""
                self.state = StateMachine.NORMAL

    def tokens( self ):
        for i in self.ret:
            yield i





def process_one_line( line ):
    sm = StateMachine()
    for c in line:
        sm.feed( c )
    for t in sm.tokens():
        yield t

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python %s <input file textfile>" % sys.argv[0])
        sys.exit(-1)

    textfile = open(sys.argv[1], "r")

    #start writing logics here
    while True:
        l = textfile.readline()
        if not l: break
        for k in process_one_line( l ):
            print( k )


