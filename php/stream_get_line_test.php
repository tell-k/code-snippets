<?php
$fp = @fopen("./data/test", "r");
if ($fp) {
    while (!feof($fp)) {
        $buffer = stream_get_line($fp, 1000000 , "\n");
//        echo number_format(memory_get_usage()) . "\n";
//        $test[] = $buffer;
    }
    fclose($fp);
}

?>
