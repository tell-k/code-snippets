<?php 
$app_id = '';
$app_secret = '';

$token_url = 'https://graph.facebook.com/oauth/access_token?'
            . 'client_id=' . $app_id 
            . '&client_secret=' . $app_secret;
            

$app_access_token = file_get_contents($token_url);
$user_id = '100002352299036';

print $app_access_token;
#$apprequest_url = "https://graph.facebook.com/"
#                . $user_id
#                . "/feeds?message=hogege" 
#                . "&data=hogehoge&"   
#                . $app_access_token
#                . "&method=post";
$apprequest_url = "https://graph.facebook.com/me/apprequests";

$result = file_get_contents($apprequest_url);
var_dump('app Request sent?', $result);
