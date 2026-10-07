# Super klaxon : onde de choc, détruit les objets proches (même la carapace bleue), renverse les karts proches
execute as @e[type=minecraft:block_display,tag=mg.kk,limit=1] at @s run particle minecraft:sonic_boom ~ ~0.8 ~ 0 0 0 0 1
execute as @e[type=minecraft:block_display,tag=mg.kk,limit=1] at @s run particle minecraft:cloud ~ ~0.5 ~ 2.5 0.3 2.5 0.15 60
execute at @e[type=minecraft:block_display,tag=mg.kk,limit=1] run playsound minecraft:item.goat_horn.sound.0 master @a[tag=mg.play,distance=..40] ~ ~ ~ 1 1
execute at @e[type=minecraft:block_display,tag=mg.kk,limit=1] run kill @e[type=minecraft:item_display,tag=mg.kshell,distance=..5.5]
execute at @e[type=minecraft:block_display,tag=mg.kk,limit=1] run kill @e[type=minecraft:item_display,tag=mg.kban,distance=..5.5]
execute at @e[type=minecraft:block_display,tag=mg.kk,limit=1] run kill @e[type=minecraft:item_display,tag=mg.kbomb,distance=..5.5]
execute at @e[type=minecraft:block_display,tag=mg.kk,limit=1] run kill @e[type=minecraft:item_display,tag=mg.kblue,distance=..6]
execute at @e[type=minecraft:block_display,tag=mg.kk,limit=1] run kill @e[type=minecraft:item_display,tag=mg.kfake,distance=..5.5]
execute as @e[type=minecraft:block_display,tag=mg.kk,limit=1] at @s as @e[type=minecraft:block_display,tag=mg.kart,tag=!mg.kk,distance=..5] run function mg:kart/owner_hit
