<?php

 $string  = '金金銀パールプレゼント金銀パールプレゼント金銀パールプレゼント金銀パールプレゼント金銀パールプレゼント金銀パールプレゼント金銀パールプレゼント金銀パールプレゼント金銀パールプレゼント金銀パールプレゼント金銀パールプレゼント金銀パールプレゼント金銀パールプレゼント金銀パールプレゼント金銀パールプレゼント金銀パールプレゼント金銀パールプレゼント金銀パールプレゼント金銀パールプレゼント金銀パールプレゼント金銀パールプレゼント金銀パールプレゼント金銀パールプレゼント金銀パールプレゼント金銀パールプレゼント金銀パールプレゼント銀パールプレゼントん';
 $string2 = mb_convert_encoding( $string, 'EUC', 'UTF-8' );
 if(preg_match("/^(\xA4[\xA1-\xA3])+$/", $string2 )){
 //if(!preg_match("/^[^\xA4\xA0-\xA4\xF4]+/", $string2 , $match)){
    print 'match success\n';
 }else{
    print "fail\n";
    // print mb_convert_encoding( prev_match_hiragana2($string2) , 'UTF-8' , 'EUC');
    print mb_convert_encoding( $match[0] , 'UTF-8' , 'EUC');
 };
 
 /**
 *
 * ある文字列中で平仮名が出てきたら, その前までの文字列を返す
 * ※出てこなかったらそのままの文字列を返す
 * ※ 2byteずつチェックして行く(EUC-JP限定)
 *
 * @param  string $string
 * @return string $prev_string
 *
 **/
 function prev_match_hiragana($string){
     $str_length  = strlen($string);
     $prev_string = null; 
     for($i = 0; $i < $str_length ; $i = $i + 2 ){
       $tmp = substr($string, $i, 2);
       if(preg_match("/^(\xA4[\xA1-\xF3])+$/", $tmp)) break;
       $prev_string .= $tmp; 
     }
     return $prev_string;
 }

 /**
 *
 * 再帰手続き(反復的プロセス)に書いてみるw
 *
 * @param  string $string
 * @return string $prev_string
 *
 **/
 function prev_match_hiragana2( $string ){
     return prev_match_hiragana2_iter($string , strlen($string));
 }
 function prev_match_hiragana2_iter( $string, $str_len, $i=0, $prev_string=null ){
     if($i >= $str_len) return $prev_string;
     if(preg_match("/^(\xA4[\xA1-\xF3])+$/", substr($string, $i, 2))) return $prev_string;
     return prev_match_hiragana2_iter($string, $str_len, $i+2, $prev_string.substr($string, $i, 2));
 }

?>


