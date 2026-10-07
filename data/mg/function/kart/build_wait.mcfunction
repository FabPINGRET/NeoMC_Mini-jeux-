# Attend que toute la zone du circuit soit chargée (60 s au plus), puis construit
execute if function mg:kart/loaded_all run return run function mg:kart/build_1
scoreboard players add $kbw mg.st 1
execute if score $kbw mg.st matches 60.. run return run tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] Circuit : zone toujours pas chargée, construction annulée.","color":"red"}]
schedule function mg:kart/build_wait 20t
