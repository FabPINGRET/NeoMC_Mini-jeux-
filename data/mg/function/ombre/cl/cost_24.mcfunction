# Œil du faucon : 50 mana, recharge 800 ticks
execute store result score $ok mg.st run function mg:ombre/mana_use {m:50}
execute unless score $ok mg.st matches 1 run return 0
scoreboard players set @s mg.olc4 800
function mg:ombre/cl/pow
function mg:ombre/cl/a24
