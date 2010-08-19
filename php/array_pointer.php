<?php

$transport = array('foot', 'bike', 'car', 'plane');
$mode = current($transport); // $mode = 'foot';
echo $mode."\n";
$mode = next($transport);    // $mode = 'bike';
echo $mode."\n";
$mode = next($transport);    // $mode = 'car';
echo $mode."\n";
$mode = prev($transport);    // $mode = 'bike';
echo $mode."\n";
array_set_pointer($transport,'bike');
$mode = current($transport); // $mode = 'foot';
echo $mode."\n";

$hoge = array(
        'key1'=>'value1',
        'key2'=>'value2',
        'key3'=>'value3',
        'key4'=>'value4',
        'key5'=>'value5',
        'key6'=>'value6',
        'key7'=>'value7',
        'key8'=>'value8',
        'key9'=>'value9',
        'key10'=>'value10',
       );
echo "----------\n";
$hoge2 = array_splice($hoge,5);
while(list($k,$v) = each($hoge2)){
   echo $k." => ".$v."\n";
}
echo "----------\n";
while(list($k,$v) = each($hoge)){
   echo $k." => ".$v."\n";
}
echo "----------\n";

function array_set_pointer(&$array, $value)
{
    reset($array);
    while($val=current($array))
    {
        if($val==$value)
            break;

        next($array);
    }
  
}

//対象の配列はこんな感じだとしよう
//6番目から処理を開始したい
$hoge = array(
        'key1'=>'value1',
        'key2'=>'value2',
        'key3'=>'value3',
        'key4'=>'value4',
        'key5'=>'value5',
        'key6'=>'value6',
        'key7'=>'value7',
        'key8'=>'value8',
        'key9'=>'value9',
        'key10'=>'value10',
       );
$hoge2 = array_splice($hoge, 5);
while(list($k,$v) = each($hoge2)){
  echo $k.'=>'.$v."\n";
}

////6番目までポインタをすすめる。
//for($i=0; $i<5; $i++){next($hoge);}
////6番目から処理
//while(list($k,$v) = each($hoge)){
//  echo $k.'=>'.$v."\n";
//}


?>
