# @s = kart : remis sur la route s'il s'y est enfoncé, nez tourné, avance selon la trajectoire (rebond si mur), caméra
execute at @s unless block ~ ~ ~ #mg:kart_pass align y run tp @s ~ ~1 ~
$execute at @s run tp @s ~ ~ ~ ~$(t) 0
execute at @s on passengers unless entity @s[type=minecraft:player] run rotate @s ~ 0
$execute at @s rotated $(h) 0 positioned ^ ^0.5 ^$(c) unless block ~ ~ ~ #mg:kart_pass run return run function mg:kart/bump {v:$(v),h:$(h)}
$execute at @s rotated $(h) 0 run tp @s ^ ^$(v) ^$(d)
$execute at @s rotated $(h) 0 positioned ^ ^2.4 ^-5 rotated ~ 16 run tp @e[type=minecraft:item_display,tag=mg.kcamc,limit=1] ~ ~ ~ ~ ~
