particle minecraft:ominous_spawning ~ ~ ~ 0 0 0 0 1

scoreboard players remove wahrog_shortray_2a Value 1
execute if score wahrog_shortray_2a Value matches 0 run function boss:mini/wahrog/attack/forking/node_2b
execute unless score wahrog_shortray_2a Value matches ..0 positioned ^ ^ ^0.1 if block ^ ^ ^ #hb_passthrough run function boss:mini/wahrog/attack/forking/ray_2a
execute unless score wahrog_shortray_2a Value matches ..0 positioned ^ ^ ^0.1 if block ^ ^ ^ blue_stained_glass run function boss:mini/wahrog/attack/forking/ray_2a
