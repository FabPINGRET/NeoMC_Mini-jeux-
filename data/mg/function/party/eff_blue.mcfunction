scoreboard players add @s mg.mpm 3
tellraw @a[tag=mg.mpp] [{"selector":"@s","color":"yellow"},{"text":" tombe sur une case ","color":"gray"},{"text":"bleue","color":"aqua","bold":true},{"text":" : +3 pièces","color":"gold"}]
execute at @s run playsound minecraft:entity.experience_orb.pickup master @a[tag=mg.mpp] ~ ~ ~ 1 1.2
execute at @s run particle minecraft:happy_villager ~ ~1 ~ 0.5 0.5 0.5 0 20
