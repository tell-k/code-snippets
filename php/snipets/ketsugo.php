<?php
define("WORK_TIME", 100);

function getmicrotime(){
    list($usec, $sec) = explode(" ",microtime());
    return ((float)$usec + (float)$sec);
}

$hoge = "abcdefghijklmn";
define("HOGE", "abcdefghijklmn");

//結合演算子の場合
$start_time = getmicrotime();
for($i = 0; $i < WORK_TIME; $i++){
    echo "hogehoge".$hoge;
//  echo memory_get_usage()."\n";
}
$time1 = sprintf("%.4f", getmicrotime() - $start_time);
echo $time1;

//sprintfの場合
//$start_time = getmicrotime();
//for($i = 0; $i < WORK_TIME; $i++){
//    $dummy = sprintf("hogehoge%s", $hoge);
//    echo memory_get_usage()."\n";
//}
//$time1 = sprintf("%.4f", getmicrotime() - $start_time);
//echo $time1;


?>
