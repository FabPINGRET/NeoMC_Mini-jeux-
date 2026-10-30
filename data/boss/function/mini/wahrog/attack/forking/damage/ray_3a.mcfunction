particle minecraft:electric_spark ~ ~ ~ 0 0 0 0 1
particle instant_effect{color:[0.000,1.000,1.000]} ~ ~ ~ 0.1 0.1 0.1 1 0 normal
function boss:mini/wahrog/attack/forking/damage/hurt

scoreboard players remove wahrog_shortray_3a Value 1
execute unless score wahrog_shortray_3a Value matches ..0 positioned ^ ^ ^0.1 if block ^ ^ ^ #hb_passthrough run function boss:mini/wahrog/attack/forking/damage/ray_3a
execute unless score wahrog_shortray_3a Value matches ..0 positioned ^ ^ ^0.1 if block ^ ^ ^ blue_stained_glass run function boss:mini/wahrog/attack/forking/damage/ray_3a
