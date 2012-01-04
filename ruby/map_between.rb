

test = [1, 2, 3, 4, 5]

def f(x)
    x.each_cons(2).map{|y,z| yield(y,z)}
end
p f(test){|x, y| x + y}
