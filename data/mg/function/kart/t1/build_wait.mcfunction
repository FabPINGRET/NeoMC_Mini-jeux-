# Attend que toute la zone du circuit soit chargée (60 s au plus), puis construit
execute if function mg:kart/t1/loaded_all run return run function mg:kart/t1/build_1
scoreboard players add $kbw mg.st 1
execute if score $kbw mg.st matches 60.. run return run tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] Circuit : zone toujours pas chargée, construction annulée.","color":"red"}]
schedule function mg:kart/t1/build_wait 20t
