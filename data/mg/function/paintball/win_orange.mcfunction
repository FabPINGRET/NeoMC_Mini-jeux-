# Victoire de l'équipe ORANGE
tag @a[team=mg_red,tag=mg.play] add mg.win
scoreboard players add @a[team=mg_red,tag=mg.play] mg.wins 1
scoreboard players set $state mg.st 3
scoreboard players set $timer mg.st 120
title @a title [{"text":"Les ORANGE gagnent !","color":"gold","bold":true}]
tellraw @a [{"text":"★ Victoire de l'équipe ","color":"gold"},{"text":"ORANGE","color":"gold","bold":true},{"text":" !","color":"gold"}]
execute as @a at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1
