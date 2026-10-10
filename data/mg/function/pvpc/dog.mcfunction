# @s achète un chien de garde (2 au maximum)
scoreboard players operation $p mg.st = @s mg.pvid
scoreboard players set $n mg.st 0
execute as @e[type=minecraft:wolf,tag=mg.pdog] if score @s mg.pvid = $p mg.st run scoreboard players add $n mg.st 1
execute if score $n mg.st matches 2.. run scoreboard players add @s mg.pco 60
execute if score $n mg.st matches 2.. run return run tellraw @s {"text":"🐺 Tu as déjà 2 chiens (remboursé).","color":"red"}
execute at @s run summon minecraft:wolf ~ ~ ~ {Tags:["mg.pdog","mg.mob","mg.pdogn"],PersistenceRequired:1b,CollarColor:14b,attributes:[{id:"minecraft:max_health",base:30d},{id:"minecraft:attack_damage",base:5d}],Health:30f}
data modify entity @e[type=minecraft:wolf,tag=mg.pdogn,limit=1] Owner set from entity @s UUID
scoreboard players operation @e[type=minecraft:wolf,tag=mg.pdogn,limit=1] mg.pvid = @s mg.pvid
tag @e[type=minecraft:wolf,tag=mg.pdogn] remove mg.pdogn
execute at @s run playsound minecraft:entity.wolf.ambient master @a ~ ~ ~ 1 1
