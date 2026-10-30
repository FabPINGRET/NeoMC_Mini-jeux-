execute if entity @s[tag=1] run kill @e[tag=wm_drone_part,tag=1,distance=0..]
execute if entity @s[tag=2] run kill @e[tag=wm_drone_part,tag=2,distance=0..]
execute if entity @s[tag=3] run kill @e[tag=wm_drone_part,tag=3,distance=0..]

execute if entity @s[tag=1] run kill @e[tag=wm_drone_draw,tag=1,distance=0..]
execute if entity @s[tag=2] run kill @e[tag=wm_drone_draw,tag=2,distance=0..]
execute if entity @s[tag=3] run kill @e[tag=wm_drone_draw,tag=3,distance=0..]

playsound minecraft:entity.iron_golem.damage hostile @a[tag=mg.flw] ~ ~ ~ 2 0.7
playsound minecraft:entity.dolphin.death hostile @a[tag=mg.flw] ~ ~ ~ 3 0.8

particle minecraft:block{block_state:"lapis_block"} ~ ~ ~ 1 1 1 0 200

function boss:9/damage
