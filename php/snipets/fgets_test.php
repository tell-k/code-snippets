<?php
echo number_format(memory_get_usage()) . "\n";
$fp = @fopen("./data/test", "r");
$test = array();
if ($fp) {
    while (!feof($fp)) {
        echo number_format(memory_get_usage()) . "\n";
        $buffer = fgets($fp, 1000);
//        $test[] = $buffer;
//        unset($test);
        sleep(1);
        echo number_format(memory_get_usage()) . "\n";
    }
    fclose($fp);
}

?>
