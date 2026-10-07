# Victoire de l'équipe JAUNE
tag @a[team=mg_yellow,tag=mg.play] add mg.win
scoreboard players add @a[team=mg_yellow,tag=mg.play] mg.wins 1
scoreboard players set $state mg.st 3
scoreboard players set $timer mg.st 120
title @a[tag=!mg.surv] title [{"text":"Les JAUNES gagnent !","color":"yellow","bold":true}]
tellraw @a [{"text":"★ Victoire de l'équipe ","color":"gold"},{"text":"JAUNE","color":"yellow","bold":true},{"text":" !","color":"gold"}]
execute as @a[tag=!mg.surv] at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1
