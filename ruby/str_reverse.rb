def str_reverse (str)
    arr = str.split(//);
    b   = arr.length - 1
    for a in 0..arr.length/2
        arr[a], arr[b-a]= arr[b-a], arr[a]
    end
    arr.join('')
end

def str_reverse2 (str)
    arr = str.split(//);
    b   = arr.length;
    for a in 0..arr.length/2
        b -= 1;
        arr[a], arr[b] = arr[b], arr[a]
    end
    arr.join('')
end

# single bytes
str = "abcded"
puts str.reverse();

#マルチバイト
$KCODE = "UTF-8"
str = "日本語文字列"
result = str_reverse str
puts result

#マルチバイト
$KCODE = "UTF-8"
str    = "日本語文字列"
result = str_reverse2 str
puts result 

