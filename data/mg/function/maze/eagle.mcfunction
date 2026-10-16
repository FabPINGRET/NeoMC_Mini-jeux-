# @s : vue d'aigle 6 s (spectateur 30 blocs au-dessus, puis retour à cette place)
execute if score @s mg.je matches 1.. run return 0
execute at @s run summon minecraft:marker ~ ~ ~ {Tags:["mg.jent","mg.jeg","mg.jegn"]}
scoreboard players operation @e[type=minecraft:marker,tag=mg.jegn] mg.jid = @s mg.jid
tag @e[tag=mg.jegn] remove mg.jegn
scoreboard players set @s mg.je 120
gamemode spectator @s
execute at @s run tp @s ~ ~30 ~ ~ 90
