# Aube sacrée : 70 mana, recharge 1200 ticks
execute store result score $ok mg.st run function mg:ombre/mana_use {m:70}
execute unless score $ok mg.st matches 1 run return 0
scoreboard players set @s mg.olc4 1200
function mg:ombre/cl/pow
function mg:ombre/cl/a44
