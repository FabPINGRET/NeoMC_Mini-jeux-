# @s commence la cinématique « open_sw »
execute if entity @s[tag=mg.olcine] run return 0
function mg:ombre/save_pos
scoreboard players set @s mg.olcs 17
scoreboard players set @s mg.olctk 0
tag @s add mg.olcine
scoreboard players operation $own mg.st = @s mg.olpid
execute in mg:ombrelune run summon minecraft:item_display -68 83 169.2 {Tags:["mg.ol","mg.olcam","mg.olcamn"],Rotation:[95.7f,44.9f],teleport_duration:2}
scoreboard players operation @e[tag=mg.olcamn] mg.olo = $own mg.st
tag @e[tag=mg.olcamn] remove mg.olcamn
gamemode spectator @s
title @s times 10 50 10
function mg:ombre/cs/lock
