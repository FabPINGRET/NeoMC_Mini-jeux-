# @s : nouveau contrat : une espèce d'une région débloquée
scoreboard players set $max mg.st 0
execute if score @s mg.olch matches 3.. run scoreboard players set $max mg.st 5
execute if score @s mg.olch matches 11.. run scoreboard players set $max mg.st 10
execute if score @s mg.olch matches 16.. run scoreboard players set $max mg.st 14
execute if score @s mg.olch matches 23.. run scoreboard players set $max mg.st 19
execute if score @s mg.olch matches 29.. run scoreboard players set $max mg.st 24
execute if score @s mg.olch matches 35.. run scoreboard players set $max mg.st 29
execute if score @s mg.olch matches 40.. run scoreboard players set $max mg.st 34
execute if score @s mg.olch matches 46.. run scoreboard players set $max mg.st 39
execute if score $max mg.st matches 0 run return run tellraw @s {"text":"📋 « Reviens quand le capitaine t'aura ouvert les routes. »","color":"gray"}
scoreboard players remove $max mg.st 1
execute store result storage mg:ombre ct.m int 1 run scoreboard players get $max mg.st
function mg:ombre/ct/rand with storage mg:ombre ct
