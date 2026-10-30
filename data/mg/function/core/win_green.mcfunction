# Victoire de l'équipe VERTE
# Seul (1 participant) : mode entraînement, pas de victoire comptée (règle commune à tous les jeux)
execute unless score $n0 mg.st matches 2.. run return run function mg:core/draw_solo
tag @a[team=mg_green,tag=mg.play] add mg.win
scoreboard players add @a[team=mg_green,tag=mg.play] mg.wins 1
scoreboard players set $state mg.st 3
scoreboard players set $timer mg.st 120
title @a[tag=!mg.surv] title [{"text":"Les VERTS gagnent !","color":"green","bold":true}]
tellraw @a [{"text":"★ Victoire de l'équipe ","color":"gold"},{"text":"VERTE","color":"green","bold":true},{"text":" !","color":"gold"}]
execute as @a[tag=!mg.surv] at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1
