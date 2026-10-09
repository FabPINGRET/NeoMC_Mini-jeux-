# Les caméléons encore cachés gagnent
scoreboard players add @a[tag=mg.cmh,tag=!mg.cmout] mg.cmpts 20
function mg:cham/recap
tag @a[tag=mg.play,tag=mg.cmh,tag=!mg.cmout] add mg.win
scoreboard players add @a[tag=mg.play,tag=mg.cmh,tag=!mg.cmout] mg.wins 1
scoreboard players set $state mg.st 3
scoreboard players set $timer mg.st 120
title @a[tag=!mg.surv] title {"text":"Les CAMÉLÉONS gagnent !","color":"green","bold":true}
tellraw @a [{"text":"★ Victoire des caméléons : ","color":"gold"},{"selector":"@a[tag=mg.play,tag=mg.cmh,tag=!mg.cmout]","color":"yellow"}]
execute as @a[tag=!mg.surv] at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1
