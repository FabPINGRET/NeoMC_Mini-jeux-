# Cri de guerre : 25 mana, recharge 400 ticks
execute store result score $ok mg.st run function mg:ombre/mana_use {m:25}
execute unless score $ok mg.st matches 1 run return 0
scoreboard players set @s mg.olc2 400
function mg:ombre/cl/pow
function mg:ombre/cl/a12
