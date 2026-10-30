# Victoire individuelle (@s = vainqueur)
# Seul (1 participant) : mode entraînement, pas de victoire comptée (règle commune à tous les jeux)
execute unless score $n0 mg.st matches 2.. run return run function mg:core/draw_solo
tag @s add mg.win
scoreboard players add @s mg.wins 1
scoreboard players set $state mg.st 3
scoreboard players set $timer mg.st 120

title @a[tag=!mg.surv] title [{"selector":"@s","color":"gold","bold":true}]
execute unless score $mp mg.st matches 1 run title @a[tag=!mg.surv] subtitle [{"text":"remporte la partie !","color":"yellow"}]
execute if score $mp mg.st matches 1 run title @a[tag=!mg.surv] subtitle [{"text":"remporte le mini-jeu !","color":"yellow"}]
execute unless score $mp mg.st matches 1 run tellraw @a [{"text":"★ ","color":"gold"},{"selector":"@s","color":"gold","bold":true},{"text":" remporte la partie !","color":"yellow"}]
execute if score $mp mg.st matches 1 run tellraw @a [{"text":"★ ","color":"gold"},{"selector":"@s","color":"gold","bold":true},{"text":" remporte le mini-jeu !","color":"yellow"}]
execute as @a[tag=!mg.surv] at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1
