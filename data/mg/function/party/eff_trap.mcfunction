# Case piège : perd une étoile (1 chance sur 4, s'il en a), sinon la moitié de ses pièces
execute at @e[type=minecraft:armor_stand,tag=mg.mpfocus,limit=1] run playsound minecraft:entity.wither.spawn master @a[tag=mg.mpp] ~ ~ ~ 0.5 1.2
execute at @e[type=minecraft:armor_stand,tag=mg.mpfocus,limit=1] run particle minecraft:large_smoke ~ ~1 ~ 0.5 0.8 0.5 0.02 40
execute store result score $ev mg.st run random value 1..4
execute if score $ev mg.st matches 1 if score @s mg.mpk matches 1.. run return run function mg:party/trap_star
scoreboard players operation @s mg.mpm /= #2 mg.st
tellraw @a[tag=mg.mpp] [{"text":"★ ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" : ☠ piège, ","color":"gray"},{"text":"moitié des pièces perdue","color":"red"}]
