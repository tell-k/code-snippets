<?php

class Test
{
    public static function call( $test )
    {
        $test = &$test;
        return ($test);
    }
}

$string = 'テストーー！！！';
echo Test::call($string);


