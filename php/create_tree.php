<?php

//下記のように三角形をechoするような再帰関数を作りなさい。
//
//    *
//   ***
//  *****
// *******
//
//for等のループ構文は使うな。
//create_leaf(4);で呼び出せるようにする。
//create_leafの中で組み込み関数は使ってよし。
//create_leafの関数は自作してもよし。
//引数は必ず１つでなくても良い。
//三角形の高さが設定できるようにする。(create_leaf(5)とかでは上の三角形が5段になる。)

function create_tree($y){
  echo create_leaf($y);
  echo create_trunk($y, null, round($y/1.1));
}
function create_leaf($y,$t=null,$c=1)
{
  if($c>$y) return $t;
  return create_leaf($y,$t.str_repeat(" ",$y-$c).str_repeat("*",$c*2-1)."\n",++$c);
}
function create_trunk($y,$t=null,$c=1)
{
  if($c>$y) return $t;
  return create_trunk($y,$t.str_repeat(" ",$y-floor($y/2.5))."|".str_repeat("*",floor($y/2.5))."|\n",++$c);
}
echo create_tree(18);


?>
