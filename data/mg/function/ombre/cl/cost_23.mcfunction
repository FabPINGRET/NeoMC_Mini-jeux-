# Piège à loups : 20 mana, recharge 240 ticks
execute store result score $ok mg.st run function mg:ombre/mana_use {m:20}
execute unless score $ok mg.st matches 1 run return 0
scoreboard players set @s mg.olc3 240
function mg:ombre/cl/pow
function mg:ombre/cl/a23
