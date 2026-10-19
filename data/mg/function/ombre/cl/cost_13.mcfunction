# Tourbillon : 30 mana, recharge 200 ticks
execute store result score $ok mg.st run function mg:ombre/mana_use {m:30}
execute unless score $ok mg.st matches 1 run return 0
scoreboard players set @s mg.olc3 200
function mg:ombre/cl/pow
function mg:ombre/cl/a13
