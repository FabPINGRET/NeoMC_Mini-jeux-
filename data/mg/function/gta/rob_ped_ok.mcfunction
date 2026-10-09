# Passant dépouillé : 20 à 80 $, il s'enfuit ; un témoin peut prévenir la police
scoreboard players set @s mg.grob 0
execute store result score $gcv mg.st run random value 20..80
function mg:gta/cash_gain
tag @e[tag=mg.grt] add mg.grobbed
effect give @e[tag=mg.grt] minecraft:speed 15 2 true
execute as @e[tag=mg.grt] at @s run particle minecraft:happy_villager ~ ~1 ~ 0.3 0.5 0.3 0 8
execute as @e[tag=mg.grt] at @s run playsound minecraft:entity.villager.hurt neutral @a ~ ~ ~ 1 1.3
execute store result score $gr mg.st run random value 0..2
execute if score $gr mg.st matches 0 run function mg:gta/wanted_up
