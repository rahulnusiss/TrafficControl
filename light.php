<IFRAME style="display:none" name="hidden-form"></IFRAME>
<h1>Set minimum and maximum time of traffic lights</h1>
<p>
<?php
$min = $_GET['minimum'];
$max = $_GET['maximum'];

  $output= shell_exec("python /home/pi/Documents/IOTCA/Init.py $min $max");

?>
<form method="get" target="hidden-form">
<hr>
Minimum
<input type="number" name="minimum" min="5" max="20" value = 10 >
<hr>
Maximum
<input type="number" name="maximum" min="25" max="100" value = 25>
<hr>
<input type="submit" value="Submit">
</form>
</body>
