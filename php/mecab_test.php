<?php
    $mecab = mecab_new();
    $str = '私の名前は船木です。';
    //echo mecab_sparse_tostr($mecab, $str);
    $node = mecab_sparse_tonode( $mecab, $str);
    while($node = mecab_node_next($node)){
        var_dump(mecab_node_feature($node));
    }
    var_dump(mecab_node_feature( mecab_node_next(mecab_node_next($node))) );
    mecab_destroy($mecab);
?>
