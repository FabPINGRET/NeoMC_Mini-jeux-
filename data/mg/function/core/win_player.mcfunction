# Victoire individuelle (@s = vainqueur)
tag @s add mg.win
scoreboard players add @s mg.wins 1
scoreboard players set $state mg.st 3
scoreboard players set $timer mg.st 120

title @a title [{"selector":"@s","color":"gold","bold":true}]
execute unless score $mp mg.st matches 1 run title @a subtitle [{"text":"remporte la partie !","color":"yellow"}]
execute if score $mp mg.st matches 1 run title @a subtitle [{"text":"remporte le mini-jeu !","color":"yellow"}]
execute unless score $mp mg.st matches 1 run tellraw @a [{"text":"★ ","color":"gold"},{"selector":"@s","color":"gold","bold":true},{"text":" remporte la partie !","color":"yellow"}]
execute if score $mp mg.st matches 1 run tellraw @a [{"text":"★ ","color":"gold"},{"selector":"@s","color":"gold","bold":true},{"text":" remporte le mini-jeu !","color":"yellow"}]
execute as @a at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1
