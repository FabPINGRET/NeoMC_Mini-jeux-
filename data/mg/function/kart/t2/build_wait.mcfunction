# Attend que toute la zone soit chargée et générée (5 min au plus), puis construit
execute if function mg:kart/t2/loaded_all run return run function mg:kart/t2/build_1
scoreboard players add $kbw2 mg.st 1
execute if score $kbw2 mg.st matches 300.. run return run tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] Royaume Koopa : zone toujours pas chargée, construction annulée.","color":"red"}]
schedule function mg:kart/t2/build_wait 20t
