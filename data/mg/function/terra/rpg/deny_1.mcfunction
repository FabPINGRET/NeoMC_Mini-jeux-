# @s n'a pas encore accès à cette région : retour au col
tp @s -29.5 68 -83.5
tellraw @s [{"text":"⛔ ","color":"red"},{"text":"Expédition non autorisée. ","color":"red","bold":true},{"text":"La Commandante Varga ouvrira ce col au chapitre « III · Le signal du marais ».","color":"gray"}]
execute at @s run playsound minecraft:block.note_block.bass player @s ~ ~ ~ 0.8 0.6
