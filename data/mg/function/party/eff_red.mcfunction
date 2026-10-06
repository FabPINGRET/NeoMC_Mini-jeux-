scoreboard players remove @s mg.mpm 3
execute if score @s mg.mpm matches ..-1 run scoreboard players set @s mg.mpm 0
tellraw @a[tag=mg.mpp] [{"selector":"@s","color":"yellow"},{"text":" tombe sur une case ","color":"gray"},{"text":"rouge","color":"red","bold":true},{"text":" : -3 pièces","color":"red"}]
execute at @e[type=minecraft:armor_stand,tag=mg.mpfocus,limit=1] run playsound minecraft:entity.villager.no master @a[tag=mg.mpp] ~ ~ ~ 1 1
execute at @e[type=minecraft:armor_stand,tag=mg.mpfocus,limit=1] run particle minecraft:angry_villager ~ ~1 ~ 0.5 0.5 0.5 0 8
