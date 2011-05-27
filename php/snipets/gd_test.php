<?php 
//header ("Content-type: image/jpeg");

$height    = 35;
$zen_width  = 600;
$rotate    = 0;
$font_size = 30;

$im = imagecreate ($zen_width,$height);
$black = ImageColorAllocate ($im, 0, 0, 0);
$white = ImageColorAllocate ($im, 255, 255, 255);

// フォントパスは環境に合わせてください。
$font1 = "/usr/share/fonts/ja/m+ipa/M+1P+IPAG-circle.ttf";

$str = "祝 丞くん誕生!!";
$str = mb_convert_encoding($str,'UTF-8','auto' );

ImageTTFText ($im, $font_size, $rotate, 0, $font_size, $white, $font1, $str);
$image_width  = imagesx($im);
$image_height = imagesy($im);

for ($y=0; $y < $image_height; $y++){
    for ($x=0; $x < $image_width; $x++){
        $index = imagecolorat($im,$x,$y);
        print ($index >0)? '■' : '□';
    }
    print '<br />';
}
//ImageJpeg($im);
ImageDestroy ($im);
?>
