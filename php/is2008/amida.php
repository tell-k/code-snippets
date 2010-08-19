<?php
$n=$argv[1];
$L='l_';
$l='l ';

echo "パターン１\n";
for($i=0;$i<$n+1;$i++){
    echo ((strlen($i)>1)?substr($i,1):$i)." ";
}
echo "\n";
for($i=0;$i<($n*2);$i++)
{
    for($j=0;$j<$n+1;$j++)
    {
        echo ($j<$i+1 && $j<$n && $i<$n)
            ?(($i%2==0 && $j%2==0)
                    ?$L:(($i%2!=0 && $j%2!=0)
                        ?$L:$l))
            :(($j<$n-($i-$n) && $j<$n && $i>=$n)
                    ?(($i%2==0 && $j%2==0)
                        ?$L:(($i%2!=0 && $j%2!=0)
                            ?$L:$l)):$l);
    }
    echo "\n";
}
for($i=$n;$i>-1;$i--){
    echo ((strlen($i)>1)?substr($i,1):$i)." ";
}

echo "\n\n";
echo "パターン２\n";
for($i=0;$i<$n+1;$i++){
    echo ((strlen($i)>1)?substr($i,1):$i)." ";
}
echo "\n";
for($i=0;$i<$n+2;$i++){
    for($j=0;$j<$n+1;$j++){
        echo ($i%2==0 && $j%2 ==0 && $j<$n && $i<$n+1)?$L:($i%2!=0 && $j%2 !=0 && $j<$n && $i<$n+1)?$L:$l;
    }
    echo "\n";
}
for($i=$n;$i>-1;$i--){
    echo ((strlen($i)>1)?substr($i,1):$i)." ";
}
echo "\n";
echo "\n";
echo "阿弥陀 = バブルソートの可視化\n";
$hoge = array(1, 2, 0, 5, 3, 4);
for($i=0;$i<count($hoge);$i++){
    echo $hoge[$i]." ";
}
echo "\n";
$height = count($hoge)-1;
for($i=0;$i<count($hoge);$i++)
{
    for($j=count($hoge)-1;$j>$i;$j--)
    { 
        if($hoge[$j] > $hoge[$j-1])
        {
            $tmp = $hoge[$j];
            $hoge[$j] = $hoge[$j-1];
            $hoge[$j-1] = $tmp;
            for($z=0; $z<count($hoge); $z++){
                echo (($j-1) == $z)?$L:$l;
            }
            echo "\n";
        }
    }
    if($i >= count($hoge)-1){
        for($z=0; $z<count($hoge); $z++){
            echo $l;
        }
        echo "\n";
    }
}
for($i=0;$i<count($hoge);$i++){
    echo $hoge[$i]." ";
}
echo "\n";
