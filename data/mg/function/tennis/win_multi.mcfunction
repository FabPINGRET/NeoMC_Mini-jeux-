# Victoire de plusieurs joueurs (un par court), même format que core/win_red
tag @a[tag=mg.tnwin,tag=mg.play] add mg.win
scoreboard players add @a[tag=mg.tnwin,tag=mg.play] mg.wins 1
scoreboard players set $state mg.st 3
scoreboard players set $timer mg.st 120
title @a[tag=!mg.surv] subtitle [{"selector":"@a[tag=mg.tnwin,tag=mg.play]","color":"yellow"}]
title @a[tag=!mg.surv] title [{"text":"🎾 Vainqueurs des courts","color":"gold","bold":true}]
tellraw @a [{"text":"★ Victoire au tennis : ","color":"gold"},{"selector":"@a[tag=mg.tnwin,tag=mg.play]","color":"yellow","bold":true},{"text":" !","color":"gold"}]
execute as @a[tag=!mg.surv] at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1
