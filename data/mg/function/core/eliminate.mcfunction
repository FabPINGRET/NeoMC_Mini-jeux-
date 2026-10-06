# Élimination générique (@s = joueur) — le perchoir ($px/$py/$pz) est défini par prepare du jeu
tag @s remove mg.play
tag @s add mg.out
scoreboard players set @s mg.deaths 0
gamemode spectator @s
execute at @s run particle minecraft:poof ~ ~1 ~ 0.3 0.5 0.3 0.05 30

execute store result storage mg:c x int 1 run scoreboard players get $px mg.st
execute store result storage mg:c y int 1 run scoreboard players get $py mg.st
execute store result storage mg:c z int 1 run scoreboard players get $pz mg.st
function mg:core/tp_perch with storage mg:c

tellraw @a [{"selector":"@s","color":"red"},{"text":" est éliminé !","color":"gray"}]
execute as @a at @s run playsound minecraft:entity.blaze.death master @s ~ ~ ~ 0.5 0.8
