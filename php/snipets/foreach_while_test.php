<?php
echo "[START]" . number_format(memory_get_usage()) . "\n";
$test_ary = array(
       'test',
       'test',
       'test',
       'test',
       'test',
);
while(list($k,$v)=each($test_ary)){
   echo "[WHILE]" . number_format(memory_get_usage()) . "\n";
}
foreach($test_ary as $k => $v){
   echo "[FOREACH]" . number_format(memory_get_usage()) . "\n";
}
echo "[END]" . number_format(memory_get_usage()) . "\n";
exit;

?>
