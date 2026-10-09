# Les cacheurs gagnent
execute unless score $n0 mg.st matches 2.. run tellraw @a[tag=mg.play] [{"text":"🎭 Fin de l'entraînement.","color":"yellow"}]
execute unless score $n0 mg.st matches 2.. run return run function mg:core/draw
tag @a[tag=mg.play,tag=mg.phh] add mg.win
scoreboard players add @a[tag=mg.play,tag=mg.phh] mg.wins 1
scoreboard players set $state mg.st 3
scoreboard players set $timer mg.st 120
title @a[tag=!mg.surv] title {"text":"Les CACHEURS gagnent !","color":"gold","bold":true}
tellraw @a [{"text":"★ Victoire des cacheurs : ","color":"gold"},{"selector":"@a[tag=mg.play,tag=mg.phh]","color":"yellow"}]
execute as @a[tag=!mg.surv] at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1
