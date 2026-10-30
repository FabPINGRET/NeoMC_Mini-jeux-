execute if entity @s[tag=1] run kill @e[tag=wm_drone_part,tag=1,tag=shield_r,distance=0..]
execute if entity @s[tag=2] run kill @e[tag=wm_drone_part,tag=2,tag=shield_r,distance=0..]
execute if entity @s[tag=3] run kill @e[tag=wm_drone_part,tag=3,tag=shield_r,distance=0..]

execute if entity @s[tag=1] run kill @e[tag=wm_drone_part,tag=1,tag=shield_l,distance=0..]
execute if entity @s[tag=2] run kill @e[tag=wm_drone_part,tag=2,tag=shield_l,distance=0..]
execute if entity @s[tag=3] run kill @e[tag=wm_drone_part,tag=3,tag=shield_l,distance=0..]

execute if entity @s[tag=1] run kill @e[tag=wm_drone_part,tag=1,tag=cannon,distance=0..]
execute if entity @s[tag=2] run kill @e[tag=wm_drone_part,tag=2,tag=cannon,distance=0..]
execute if entity @s[tag=3] run kill @e[tag=wm_drone_part,tag=3,tag=cannon,distance=0..]

playsound minecraft:entity.iron_golem.damage hostile @a[tag=mg.flw] ~ ~ ~ 2 0.7
particle minecraft:block{block_state:"granite"} ~ ~ ~ 1 1 1 0 200
