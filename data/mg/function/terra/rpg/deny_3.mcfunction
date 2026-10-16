# @s n'a pas encore accès à cette région : retour au col
tp @s -83.5 68 6.5
tellraw @s [{"text":"⛔ ","color":"red"},{"text":"Expédition non autorisée. ","color":"red","bold":true},{"text":"La Commandante Varga ouvrira ce col au chapitre « VI · Le vol de la cellule ».","color":"gray"}]
execute at @s run playsound minecraft:block.note_block.bass player @s ~ ~ ~ 0.8 0.6
