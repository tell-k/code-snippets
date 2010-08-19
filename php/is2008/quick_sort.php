<?php
$hoge = array(1, 2, 3, 5, 10);
//function quick_sort($hoge){
//    if(count($hoge) <= 1){
//        return $hoge;
//    }
//    $pivot = $hoge[floor(count($hoge)/2)];
//
//    $right = array(); 
//    $left = array();
//    for($i=0; $i< count($hoge) ; $i++)
//    {
//        if($i == floor(count($hoge)/2))
//            continue;
//
//        if($hoge[$i] <= $pivot){
//            $left[]  = $hoge[$i];
//        }else{
//            $right[] = $hoge[$i];
//        }
//    }
//    return array_merge(quick_sort($left),array($pivot),quick_sort($right));
//}
//print_r(quick_sort($hoge));
//
function quick_sort(&$hoge, $l_idx=0, $r_idx=null)
{
    if($r_idx === null) $r_idx = count($hoge)-1;

    //終了条件
    if($l_idx >= $r_idx){
        return;
    }

    $pivot = $hoge[$r_idx];
    $i = $l_idx-1;
    $j = $r_idx;
    while(1){
        while(isset($hoge[++$i]) && $hoge[$i] < $pivot);
        while(isset($hoge[--$j]) && $hoge[$j] > $pivot);
        if($i >= $j) break;
        //swap
        $tmp = $hoge[$i]; 
        $hoge[$i] = $hoge[$j]; 
        $hoge[$j] = $tmp; 
    }
    //swap
    $tmp          = $hoge[$i]; 
    $hoge[$i]     = $hoge[$r_idx]; 
    $hoge[$r_idx] = $tmp; 

    quick_sort($hoge, $l_idx, $i-1);
    quick_sort($hoge, $i+1, $r_idx);
}
quick_sort($hoge);
print_r($hoge);
echo memory_get_peak_usage();

