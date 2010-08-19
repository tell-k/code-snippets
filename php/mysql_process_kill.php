<?php

$link = mysql_connect('localhost', 'kida', 'redhot2006');

$result = mysql_list_processes($link);
while ($row = mysql_fetch_assoc($result)){
    printf("%s %s %s %s %s\n", $row["Id"], $row["Host"], $row["db"],
        $row["Command"], $row["Time"]);
}

sleep(60);
mysql_free_result($result);

?>
