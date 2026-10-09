# @s : marqueur — jeu gagné par le côté 2 ; le service change de camp
scoreboard players add @s mg.tng2 1
scoreboard players set @s mg.tnp1 0
scoreboard players set @s mg.tnp2 0
scoreboard players set $tnq mg.st 3
scoreboard players operation $tnq mg.st -= @s mg.tnl
scoreboard players operation @s mg.tnl = $tnq mg.st
scoreboard players operation $tnq mg.st = @s mg.tng2
execute as @a[tag=mg.tnk,scores={mg.tns=2}] run scoreboard players operation @s mg.tngw = $tnq mg.st
execute if entity @e[type=minecraft:mannequin,tag=mg.tnrob,tag=mg.tnk,scores={mg.tns=2}] run scoreboard players operation Robot mg.tngw = $tnq mg.st
title @a[tag=mg.tnk] title [{"text":"Jeu ","color":"gold"},{"text":"ROUGE","color":"red","bold":true}]
tellraw @a[tag=mg.tnk] [{"text":"🎾 Jeu pour ","color":"gold"},{"selector":"@e[tag=mg.tnk,scores={mg.tns=2}]","color":"red"},{"text":" — jeux ","color":"gray"},{"score":{"name":"@s","objective":"mg.tng1"},"color":"aqua"},{"text":"-","color":"gray"},{"score":{"name":"@s","objective":"mg.tng2"},"color":"red"}]
execute as @a[tag=mg.tnk] at @s run playsound minecraft:entity.player.levelup master @s ~ ~ ~ 0.6 1.3
scoreboard players set $tnw mg.st 2
execute if score @s mg.tng2 matches 3.. run function mg:tennis/court_win
