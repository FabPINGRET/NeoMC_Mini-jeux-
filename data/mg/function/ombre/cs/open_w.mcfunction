# @s commence la cinématique « open_w »
execute if entity @s[tag=mg.olcine] run return 0
function mg:ombre/save_pos
scoreboard players set @s mg.olcs 10
scoreboard players set @s mg.olctk 0
tag @s add mg.olcine
scoreboard players operation $own mg.st = @s mg.olpid
execute in mg:ombrelune run summon minecraft:item_display -68 82 0 {Tags:["mg.ol","mg.olcam","mg.olcamn"],Rotation:[90.0f,45.0f],teleport_duration:2}
scoreboard players operation @e[tag=mg.olcamn] mg.olo = $own mg.st
tag @e[tag=mg.olcamn] remove mg.olcamn
gamemode spectator @s
title @s times 10 50 10
function mg:ombre/cs/lock
