<?php

echo"<pre>";
system("snmpwalk -Os -c public -v 1 localhost|head");
echo"</pre>";

?>