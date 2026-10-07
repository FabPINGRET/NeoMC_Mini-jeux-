scoreboard players remove @s mg.t 1
execute if score @s mg.t matches 1.. run return 0
tag @s remove mg.kdead
data merge entity @s {start_interpolation:0,interpolation_duration:6,transformation:{scale:[1.2f,1.2f,1.2f]}}
