<?php

function my_array_reverse(&$test)
{
   for($i=count($test)-1; $i >= count($test)/2;$tmp=$test[count($test)-1-$i],$test[count($test)-1-$i]=$test[$i],$test[$i]=$tmp, $i--);
}
$test = array(1,2,3,4,5,6,0,7,8,9,10);
var_dump(my_array_reverse($test));
var_dump($test);
for($i=count($test)-1; $i >= count($test)/2;$tmp=$test[count($test)-1-$i],$test[count($test)-1-$i]=$test[$i],$test[$i]=$tmp, $i--);
var_dump($test);
