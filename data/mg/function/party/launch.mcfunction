# Lance le mini-jeu tiré (comme si l'admin l'avait choisi) ; core/return_lobby reviendra au plateau
function mg:party/pick
title @a reset
clear @a minecraft:echo_shard
execute as @a[tag=mg.mpp] run function mg:core/attr_reset
scoreboard players set $mpl mg.st 1
scoreboard players set $state mg.st 0
execute if entity @a[tag=mg.mpa] as @a[tag=mg.mpa,limit=1] run function mg:party/launch_as
execute unless entity @a[tag=mg.mpa] as @a[tag=mg.mpp,limit=1] run function mg:party/launch_as
scoreboard players set $mpl mg.st 0
execute if score $state mg.st matches 0 as @a[tag=mg.mpp] run function mg:core/reset_player
execute if score $state mg.st matches 0 run function mg:party/end
execute if score $state mg.st matches 0 run tellraw @a [{"text":"[Mini Party] Plus aucun participant : partie arrêtée.","color":"red"}]
