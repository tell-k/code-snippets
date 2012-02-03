#!/usr/bin/env python
#-*- coding:utf8 -*-

def ascii2ebcdic_sign_number(number):
    plus_codes = {0:'{', 1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I'}
    minus_codes = {1:'J', 2:'K', 3:'L', 4:'M', 5:'N', 6:'O', 7:'P', 8:'Q', 9:'R'}
    codes = plus_codes if number < 0 else minus_codes
    return str(abs(number))[:-1] + codes[abs(number) % 10]

print ascii2ebcdic_sign_number(1001) #=> 100J
print ascii2ebcdic_sign_number(-1001) #=> 100A

#function convertEbcdicSignNumber($number)
#{
#    //数値がプラスの場合
#    $plus_map= array(
#        '0' => '{',
#        '1' => 'A',
#        '2' => 'B',
#        '3' => 'C',
#        '4' => 'D',
#        '5' => 'E',
#        '6' => 'F',
#        '7' => 'G',
#        '8' => 'H',
#        '9' => 'I',
#    );
#    //数値がマイナスの場合
#    $minus_map = array(
#    );
#
#    $convert_map = ($number >= 0)?$plus_map:$minus_map;
#    $number = ($number >= 0)?(string)$number:(string)abs($number);
#    $n_len  = strlen($number);
#    if(array_key_exists($number[$n_len-1], $convert_map)){
#       $number[$n_len-1] = $convert_map[$number[$n_len-1]];
#    }else{
#       return "false";
#    }
#    return $number;
#}
#
#echo "↓の結果をddコマンドでEBCDICコードに変換すればおｋ！\n";
#echo convertEbcdicSignNumber(1235) ."\n";
#echo convertEbcdicSignNumber(-1235) ."\n";



