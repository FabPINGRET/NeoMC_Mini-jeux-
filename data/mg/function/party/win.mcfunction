# Vainqueur de la Mini Party (@s) : +1 victoire, célébration
tag @s add mg.win
scoreboard players add @s mg.wins 1
scoreboard players set $state mg.st 3
scoreboard players set $timer mg.st 160
title @a times 10 100 20
title @a title [{"text":"🏆 ","color":"gold"},{"selector":"@s","color":"gold","bold":true}]
title @a subtitle [{"text":"remporte la MINI PARTY avec ","color":"yellow"},{"score":{"name":"@s","objective":"mg.mpk"},"color":"yellow","bold":true},{"text":" ★ et ","color":"yellow"},{"score":{"name":"@s","objective":"mg.mpm"},"color":"gold","bold":true},{"text":" pièces","color":"yellow"}]
tellraw @a [{"text":"🏆 ","color":"gold"},{"selector":"@s","color":"gold","bold":true},{"text":" remporte la MINI PARTY !","color":"yellow","bold":true}]
execute as @a at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1
execute as @a at @s run playsound minecraft:entity.firework_rocket.large_blast master @s ~ ~ ~ 1 1
