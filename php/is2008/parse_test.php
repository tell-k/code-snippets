<?php
require_once "HTTP/Request.php";

// HTTP_Requestの初期化
$url = "http://dailynews.yahoo.co.jp/fc/economy/student_jobhunting/?1220950500";

//TOPページのURL
$token = preg_split('/\//',$url);
$top_url = $token[0].'//'.$token[1].$token[2];

//相対パス付URL
$relative_url = substr($url,0, strlen($url)-strlen(basename($url)));

$http = new HTTP_Request($url);
$http->addHeader("User-Agent", "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)");

// HTTPリクエスト実行
$response = $http->sendRequest();
$response_body = $http->getResponseBody();
//$response_body = mb_convert_encoding($http->getResponseBody(),'UTF-8', 'EUC-JP');

$words = array(
        'キャノン',
        'SED',
        '朝日',
        'テレビ',
        );

foreach($words as $v){
   $target[] = "/$v/i";
   $replace[] = '<span style="background-color:#daa; border:1px solid #F00;">'.$v.'</span>';
}

echo unhtml_replace($target, $replace, $response_body, $top_url, $relative_url);
exit;

function unhtml_replace($search, $replace, $subject, $top_url, $relative_url) {

    $split = array_chunk(preg_split("/<(.*?)>/",$subject, -1, PREG_SPLIT_DELIM_CAPTURE),2);
    $subject = '';
    $start_flg=0;
    foreach ($split as $tokens){
        //tokenの中から、src or hrefがあるものだけ抽出
        if(isset($tokens[1]) && preg_match('/(.*)(src|href)=(\"|\')(.*)/',$tokens[1],$matches)){
          //src href 直後がhttpから始まってたら虫。
          if(!preg_match('/^(http|https)/',$matches[4])){
             //ルート相対から始まってなかったら、relative_urlをくっつける。
             if(!preg_match('/^\//',$matches[4])){
                $tokens[1]=$matches[1].$matches[2]."=".$matches[3].$relative_url.$matches[4];

             //ルート相対から始まってたらtop_urlをくっつける。
             }else{
                $tokens[1]=$matches[1].$matches[2]."=".$matches[3].$top_url.$matches[4];
             }
          }
        }

        if(isset($tokens[1]) && preg_match('/\/head/i',$tokens[1])){
            $start_flg=1; 
        }
        if($start_flg){
            $subject .= preg_replace($search, $replace, $tokens[0]).
            (isset($tokens[1]) ? '<'.$tokens[1].'>':'');
        }else{
            $subject .= $tokens[0].(isset($tokens[1]) ? '<'.$tokens[1].'>':'');
        }
    }
    return $subject;
}

