<?php

if (defined('STDIN')) {
        $shwitchname = $argv[1];
} else {
        $shwitchname = $_GET['shwitchname'];
}

switch ($shwitchname) {
case "garagedooropen":
	exec('python /usr/lib/cgi-bin/garage-door.py garagedoor open > /dev/null 2>&1 &');
	echo "Opening garage door.";
	break;
case "garagedoorclose":
	exec('python /usr/lib/cgi-bin/garage-door.py garagedoor close > /dev/null 2>&1 &');
	echo "Closing garage door.";
	break;
case "on":
        exec('python /usr/lib/cgi-bin/switches.py on > /dev/null 2>&1 &');
        echo "Turning switch on.";
        $fp = fopen('christmas.txt', 'w');
        fwrite($fp, 'Switch On');
        fclose($fp);
        break;
}

?>

