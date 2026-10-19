# Lumière guérisseuse : 18 mana, recharge 120 ticks
execute store result score $ok mg.st run function mg:ombre/mana_use {m:18}
execute unless score $ok mg.st matches 1 run return 0
scoreboard players set @s mg.olc1 120
function mg:ombre/cl/pow
function mg:ombre/cl/a41
