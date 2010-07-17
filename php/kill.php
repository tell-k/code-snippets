<?php

$mysqli = new mysqli("localhost", "kida", "redhot2006", "test");

/* 接続状況をチェックします */
if (mysqli_connect_errno()) {
    printf("Connect failed: %s\n", mysqli_connect_error());
    exit();
}

/* スレッド ID を取得します */
$thread_id = $mysqli->thread_id;
echo $thread_id;
/* 接続を終了します */
//$mysqli->kill($thread_id);


?>

