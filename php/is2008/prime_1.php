<?php
//素数判定

for($i=0; $i<100; $i++) {
    echo (is_prime($i+1))? "prime => ".($i+1)."\n" : "not prime => ".($i+1)."\n";
}

function is_prime($num) {
  if ($num < 2) return false;
  for ($i = 2; $i < $num; $i++){ if(!($num%$i)){ return false;}}
  return true;
}

