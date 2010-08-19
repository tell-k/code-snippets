<?php

//ref http://d.hatena.ne.jp/cloned/20060510
class Hoge
{
    public static $value = "default";
    public static function &getValue()
    {
        return self::$value;
    }
}
class Fuga
{
    public static function &getValue()
    {
        $value =& Hoge::getValue();
        return $value;
    }
}
$v =& Fuga::getValue();
$v = "HelloWorld";
print Hoge::$value;
