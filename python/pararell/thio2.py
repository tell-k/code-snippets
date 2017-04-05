
import cProfile

BIG_NUMBER = 1000000
NUMBERS = [
    100000000,
    10000,
    20000,
    10000,
    10000,
    200000000,
    10000,
    90000,
    10000,
    10000,
    80000,
    10000,
    10000,
    1000000,
    10000,
    20000,
    10000,
    10000,
    30000,
]


def write_dummy(fileno, number):
    with open("dummy/dummy%d.txt" % fileno, "w") as fp:
        for j in xrange(number):
            fp.write("line %d\n" % j)

def main():
    for i in xrange(len(NUMBERS)):
        write_dummy(i + 1, NUMBERS[i])

if __name__ == "__main__":
    cProfile.run("main()")
