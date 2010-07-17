<?php
$a =10000;
call_user_func(create_function('$a', 'echo $a;'), $a);

?>
