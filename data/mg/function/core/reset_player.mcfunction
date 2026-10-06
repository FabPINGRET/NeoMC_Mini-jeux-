# Remise à zéro d'un joueur → lobby (@s = joueur)
tag @s remove mg.play
tag @s remove mg.out
tag @s remove mg.win
tag @s remove mg.visit
tag @s remove mg.rsp
team leave @s
gamemode adventure @s
effect clear @s
function mg:core/attr_reset
clear @s
function mg:core/give_menu
spawnpoint @s 0 64 0
tp @s 0.5 64 0.5 facing 0.5 64 8.5
scoreboard players set @s mg.deaths 0
