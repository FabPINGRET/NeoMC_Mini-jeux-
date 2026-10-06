scoreboard players add @s mg.mpm 3
tellraw @a[tag=mg.mpp] [{"selector":"@s","color":"yellow"},{"text":" tombe sur une case ","color":"gray"},{"text":"bleue","color":"aqua","bold":true},{"text":" : +3 pièces","color":"gold"}]
execute at @e[type=minecraft:armor_stand,tag=mg.mpfocus,limit=1] run playsound minecraft:entity.experience_orb.pickup master @a[tag=mg.mpp] ~ ~ ~ 1 1.2
execute at @e[type=minecraft:armor_stand,tag=mg.mpfocus,limit=1] run particle minecraft:happy_villager ~ ~1 ~ 0.5 0.5 0.5 0 20
