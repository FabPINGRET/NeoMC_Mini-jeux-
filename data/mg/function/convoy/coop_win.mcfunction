# Coop : convoi livré
kill @e[tag=mg.cvm]
tag @a[tag=mg.play] add mg.win
scoreboard players add @a[tag=mg.play] mg.wins 1
scoreboard players set $state mg.st 3
scoreboard players set $timer mg.st 120
title @a[tag=!mg.surv] title {"text":"CONVOI LIVRÉ !","color":"gold","bold":true}
tellraw @a {"text":"★ Le convoi est arrivé à bon port — bravo à l'escorte !","color":"gold"}
execute as @a[tag=!mg.surv] at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1
