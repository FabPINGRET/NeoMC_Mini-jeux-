# Retour au plateau après un mini-jeu (fin de core/return_lobby)
scoreboard players add $mpround mg.st 1
scoreboard players set $game mg.st 59
scoreboard players set $state mg.st 2
execute as @a[tag=mg.mpp,tag=!mg.spectate] run function mg:party/rejoin
function mg:party/hud
function mg:party/bar_update
scoreboard players set $mpu mg.st 0
execute if score $mpround mg.st > $mpmax mg.st run return run function mg:party/final
scoreboard players set $mpt mg.st 1
scoreboard players set $mph mg.st 0
function mg:party/round_title
