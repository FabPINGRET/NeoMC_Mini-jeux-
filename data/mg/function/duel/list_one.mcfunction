# Un candidat (@s = joueur listé ; le demandeur porte mg.dlq) : numéro, occupé ?, ligne cliquable
function mg:duel/busy
execute if score $dlb mg.st matches 1 run return 0
execute if entity @s[tag=mg.dlrq] run return 0
execute if score @s mg.dlto matches 1.. run return 0
execute unless score @s mg.dlid matches 1.. run function mg:duel/new_id
scoreboard players add $dlc mg.st 1
scoreboard players operation #dll mg.st = @s mg.dlid
scoreboard players add #dll mg.st 1000
execute store result storage mg:duel m.v int 1 run scoreboard players get #dll mg.st
function mg:duel/list_line with storage mg:duel m
