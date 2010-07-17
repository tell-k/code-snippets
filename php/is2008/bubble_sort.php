<?php

$hoge = array(0, 1, 2, 3, 4, 5);
function bubble_sort($hoge, $order='asc'){
    for($i=0;$i<count($hoge);$i++)
    {
      for($j=count($hoge)-1;$j>$i;$j--)
      {
        switch($order){
          case 'asc':
            if($hoge[$i] > $hoge[$j])
            { 
              $tmp = $hoge[$i];
              $hoge[$i] = $hoge[$j];
              $hoge[$j] = $tmp;
            }
            break;
          case 'desc':
            if($hoge[$i] < $hoge[$j])
            {
              $tmp = $hoge[$i];
              $hoge[$i] = $hoge[$j];
              $hoge[$j] = $tmp;
            }
            break;
        }
        echo "\n";
      }
    }
    return $hoge;
}
var_dump(bubble_sort($hoge, 'desc'));
