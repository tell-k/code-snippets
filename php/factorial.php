<?php

//(define (factorial n)
//  (if (= 0 n)
//      1
//      (* n (factorial (- n 1)))))
print fact_iter(100)."\n";

function fact_recur($n){
  if($n == 0){
     return 1;
  }
  //echo number_format(memory_get_usage()) . "\n";
  return $n*fact_recur($n-1);
}

function fact_iter($n,$product=1,$counter=1){
  if($counter > $n){
     return $product;
  }
  //echo number_format(memory_get_usage()) . "\n";
  return fact_iter($n,$product*$counter,++$counter);
}

?>
