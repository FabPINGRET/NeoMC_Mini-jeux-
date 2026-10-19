# Jugement de l'Aube : 60 mana, recharge 900 ticks
execute store result score $ok mg.st run function mg:ombre/mana_use {m:60}
execute unless score $ok mg.st matches 1 run return 0
scoreboard players set @s mg.olc4 900
function mg:ombre/cl/pow
function mg:ombre/cl/a14
