# @s = kart : remis sur la route s'il s'y est enfoncé, tourné, puis avancé (sauf mur devant : rebond)
execute at @s unless block ~ ~ ~ #mg:kart_pass align y run tp @s ~ ~1 ~
$execute at @s run tp @s ~ ~ ~ ~$(t) 0
$execute on passengers if entity @s[type=minecraft:block_display] run rotate @s ~$(t) ~
$execute at @s rotated ~ 0 positioned ^ ^0.5 ^$(c) unless block ~ ~ ~ #mg:kart_pass run return run function mg:kart/bump {v:$(v)}
$execute at @s rotated ~ 0 run tp @s ^ ^$(v) ^$(d)
