# Lance de givre : 15 mana, recharge 100 ticks
execute store result score $ok mg.st run function mg:ombre/mana_use {m:15}
execute unless score $ok mg.st matches 1 run return 0
scoreboard players set @s mg.olc2 100
function mg:ombre/cl/pow
function mg:ombre/cl/a32
