<?php
$str = 'abcde';
var_dump(str_reverse($str));

$str = 'abcde';
var_dump(strrev($str));

#マルチバイト(UTF-8)
$str = '日本語';
var_dump(mb_str_reverse2($str));

#マルチバイト
$str = '日本語';
var_dump(mb_str_reverse($str));

function mb_str_reverse2 ($str) {
    return implode('', array_reverse(preg_split('//u', $str)));
}

function mb_str_reverse ($str) {
    $str = mb_str_to_array($str);
    $b   = count($str);
    for($a = 0; $a < --$b; $a++){
       list($str[$a], $str[$b]) = array($str[$b], $str[$a]);
    }
    return implode('', $str);
}

function str_reverse ($str) {
    $b = strlen($str);
    for($a = 0; $a < --$b; $a++) {
       list($str[$a], $str[$b]) = array($str[$b], $str[$a]);
    }
    return $str;
}

function mb_str_to_array($str) {
    $stop   = mb_strlen($str);
    $result = array();
    for($idx = 0; $idx < $stop; $idx++) {
        $result[] = mb_substr($str, $idx, 1);
    }
    return $result;
}
