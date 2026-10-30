execute as @e[tag=lod_boss_loc,distance=0..] at @s run tp @s @e[limit=1,tag=lod_boss_target,distance=0..]

setblock -10083 134 -211 minecraft:air

setblock -10083 134 -209 minecraft:air

kill @e[tag=temp_target,distance=0..]
tag @e[tag=lod_boss_target,distance=0..] remove lod_boss_target


summon area_effect_cloud ~ ~ ~ {Tags:["bite_direc","1","exclude"]}
summon area_effect_cloud ~ ~ ~ {Tags:["bite_direc","2","exclude"]}

tag @e[type=minecraft:area_effect_cloud,tag=bite_direc,limit=1,sort=random,distance=0..] remove exclude

kill @e[type=minecraft:area_effect_cloud,tag=bite_direc,tag=exclude,distance=0..]

execute if entity @e[tag=bite_direc,tag=1,distance=0..] run setblock -10083 134 -207 minecraft:redstone_block
execute if entity @e[tag=bite_direc,tag=2,distance=0..] run setblock -10083 134 -205 minecraft:redstone_block

kill @e[type=minecraft:area_effect_cloud,tag=bite_direc,distance=0..]
