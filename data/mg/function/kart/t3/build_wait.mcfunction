execute if function mg:kart/t3/loaded_all run return run function mg:kart/t3/build_1
scoreboard players add $kbw3 mg.st 1
execute if score $kbw3 mg.st matches 300.. run return run tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] Forteresse Bob-omb : zone pas chargée, construction annulée.","color":"red"}]
schedule function mg:kart/t3/build_wait 20t
