<?php

$xml = @file_get_contents("./data/test.xml");
$xml = explode("\n", $xml);
var_dump($xml);
//while () {
//    $buffer = stream_get_line($fp, 4096);
//    //echo $buffer;
//}
