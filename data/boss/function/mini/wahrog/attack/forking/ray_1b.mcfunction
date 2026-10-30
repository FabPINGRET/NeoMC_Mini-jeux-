particle minecraft:ominous_spawning ~ ~ ~ 0 0 0 0 1

scoreboard players remove wahrog_shortray_1b Value 1
#execute if score wahrog_shortray_1b Value matches 0 run function boss:mini/wahrog/attack/forking/node_1b
execute unless score wahrog_shortray_1b Value matches ..0 positioned ^ ^ ^0.1 if block ^ ^ ^ #hb_passthrough run function boss:mini/wahrog/attack/forking/ray_1b
execute unless score wahrog_shortray_1b Value matches ..0 positioned ^ ^ ^0.1 if block ^ ^ ^ blue_stained_glass run function boss:mini/wahrog/attack/forking/ray_1b
