# @s commence la cinématique « pass_e »
execute if entity @s[tag=mg.trcine] run return 0
function mg:terra/save_pos
scoreboard players set @s mg.trcs 3
scoreboard players set @s mg.trct 0
tag @s add mg.trcine
scoreboard players operation $own mg.st = @s mg.tvpid
execute in mg:terranova run summon minecraft:item_display 76 75 30 {Tags:["mg.tv","mg.trcam","mg.trcamn"],Rotation:[-90.0f,23.2f],teleport_duration:2}
scoreboard players operation @e[tag=mg.trcamn] mg.tvo = $own mg.st
tag @e[tag=mg.trcamn] remove mg.trcamn
gamemode spectator @s
title @s times 10 50 10
function mg:terra/rpg/cs/lock
