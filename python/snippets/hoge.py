
taka = "taka.txt"
tora = "tora.txt"
batta = "batta.txt"

hoge = lambda x, y, z: open(taka, "r"), open(tora, "w"), open(batta, "w")

def hoge():
    return (open(taka, "r") as ta)

with open(taka, "r") as ta, open(tora, "w") as to, open(batta, "w") as ba:

    print taka
    print tora
    print batta

    pass


with (
     open(taka, "r"),
     open(tora, "w"),
     open(batta, "w")
     ), as ta, to, ba:

    pass
