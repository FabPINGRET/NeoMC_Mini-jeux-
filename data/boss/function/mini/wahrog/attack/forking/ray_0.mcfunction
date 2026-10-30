particle minecraft:ominous_spawning ~ ~ ~ 0 0 0 0 1

scoreboard players remove wahrog_shortray Value 1
execute if score wahrog_shortray Value matches 0 run function boss:mini/wahrog/attack/forking/node_1
execute if score wahrog_shortray Value matches 0 run function boss:mini/wahrog/attack/forking/node_1a
execute unless score wahrog_shortray Value matches ..0 positioned ^ ^ ^0.1 if block ^ ^ ^ #hb_passthrough run function boss:mini/wahrog/attack/forking/ray_0
execute unless score wahrog_shortray Value matches ..0 positioned ^ ^ ^0.1 if block ^ ^ ^ blue_stained_glass run function boss:mini/wahrog/attack/forking/ray_0
