import threading
import cProfile

BIG_NUMBER = 1000000

class YourThreadSubclass(threading.Thread):

    def __init__(self, fileno, number):
        threading.Thread.__init__(self)
        self.fileno = fileno
        self.number = number

    def run(self):
        with open('dummy/dummy%d.txt' % self.fileno, 'r') as fp:
            fp.read()
#            for j in xrange(self.number):
#                fp.write('line %d\n' % j)

def main():
    threads = [YourThreadSubclass(i + 1, NUMBERS[i]) for i in xrange(len(NUMBERS))]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

if __name__ == "__main__":
    cProfile.run("main()")

