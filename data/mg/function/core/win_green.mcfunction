# Victoire de l'équipe VERTE
tag @a[team=mg_green,tag=mg.play] add mg.win
scoreboard players add @a[team=mg_green,tag=mg.play] mg.wins 1
scoreboard players set $state mg.st 3
scoreboard players set $timer mg.st 120
title @a title [{"text":"Les VERTS gagnent !","color":"green","bold":true}]
tellraw @a [{"text":"★ Victoire de l'équipe ","color":"gold"},{"text":"VERTE","color":"green","bold":true},{"text":" !","color":"gold"}]
execute as @a at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1
